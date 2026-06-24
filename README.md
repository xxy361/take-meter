# Take Meter

 A fine-tuned text classifier that evaluates discourse quality in an online community.


 ## File Structure

```
take-meter/
├── planning.md                      # Planning doc
├── README.md                        # This file
├── takemeter.ipynb                  # Fine-tuning + evaluation notebook
├── scripts/
│   └── build_balanced_dataset.py    # Combines & samples the balanced dataset
└── data/
    ├── megathread_jun26.csv         # Annotated thread #1
    ├── megathread_jun24.csv         # Annotated thread #2
    └── balanced_dataset.csv         # Final balanced set, 200 rows (text, label)
```



## Tools and Setup

| Component          | Tool                                         | Notes                                                        |
| ------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| Base model         | `distilbert-base-uncased`                    | HuggingFace — free to download, no account needed            |
| Fine-tuning        | Google Colab (free GPU)                      | Free T4 GPU; fine-tuning DistilBERT on 200 examples takes ~5–15 min |
| Training libraries | `transformers` + `datasets` + `scikit-learn` | Pre-installed on Colab — no setup needed                     |
| Baseline LLM       | Groq (`llama-3.3-70b-versatile`)             | Free tier                                                    |



### Choice of Community

The community chosen is **Genshin Impact**, particular the **Megathread section for Team/Character building**. This is a good fit for a classification task because each post has many comments of varied quality and mainly text based. Even though the threads focus the same topic of team/character building, the disclosure still varies greatly as people could provide advice, discuss numbers and stats, ask for help, reference info from the game itself, tell personal experience, express preference of characters, etc. Classifying each comment could help filtering out actual useful advice/strategy vs. subjective opinion/preferences.



### Taxonomy

**Labels:** What are your 2–4 labels? Define each in a complete sentence. Include 2 example posts per label.

| Label       | Definition                                                   | Examples                                                     | Uncertain Cases                                              |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Analysis    | A post that explains or recommends team building strategy using evidence, calculations, comparisons, or detailed justification. | Example 1:<br />"My mavuika (C0R1) who is not particulary boosted (is ok, but not too op) is siting in 55/200 crit, with EM sands. Consider that obsidian codex can bring you up to 40Crate, you should avoid to surpass 60C.rate, and redistribute as much as you can into C.dmg or atk.<br/><br/>Be carefull with becon since it will already give you around 30% c.rate, so you should focus more on just atk and c.dmg. I think, that something around 50/180-200 should be doable without too much grind. "<br /><br />Example 2:<br />"I would probably go for Nicole (buff + shield) + Fischl (bow + damage) + Bennett (buff + heal just in case) + any Claymore you like the most  (Dehya / Dori / Noelle / Razor / Aino, although i would focus on either Razor or Dehya, with Razor being slightly preferred as he is Hexerei)." | "Pick which ever you like more in this case.<br/>Columbina is an amazing lunar support and you seem to have most of her team in the bag already, just slap someone in that fourth slot.<br/>Citlali is an amazing hydro and pyro support, with good cryo application and relevance in the Schneznaya meta.<br/>Either could be justified, but if you want my personal opinion, I'd say go for Citlali because she has a skin coming out. (and i love her to death)"<br />This example comment contains both analysis and opinion. However, it would be classified into "Analysis", because the main message here is that either character would work based on reasonable comparison. Though containing personal opinion, this comment is recommending the player to use their personal preference as a tie-breaker when both characters are equally suitable to the team. |
| Opinion     | A post that expresses a personal preference or judgment without significant supporting evidence or analysis. | Example 1: <br />"Prune. Sucrose is only better at c6    "<br /><br />Example 2:<br />"mualani / mavuika / mona / sucrose is mualani’s best team! if you don’t  have mona yet (you can get her in the anniversary in september), use  kachina instead!" | "Mavuika is a better pick IF you get Natlan teammate later<br/><br/>well you got Durin, so Lohen is ok. you can add Albedo too i guess. not sure of full team"<br/>This comment would be classified as "Opinion", because even though the author is giving a recommendation, the comment is not supported with concrete reasoning such as character buff, damage performance, etc. |
| Information | A post that shares factual information, resources, announcements, or references without argument. | Example 1: <br />"For early game and overworld exploration, any character can work (including the starter trio) as long as they're properly leveled up. Infographic of Build Order Priority based on WL/AR<br /><br />You can check sites like keqingmains or crimsonwitch for gearing. KQM also has a newbie guide that talks briefly about team building, too."<br /><br />Example 2:<br />"An artifact 4pc set called "Scroll of the Hero of Cinder City", obtainable in Natlan's artifact domain." | "The Lunar Crit Dmg buff from the weapon only applies to the wielder, so Nefer will not get the buff. Only Barbara gets the buff, but she doesn't benefit from it. Also it will not show up in her stats, as it's different from the normal Crit Dmg.<br/>Btw is Nefer using her own signature weapon (Reliquary of Truth)?"<br />Though the example comment above ends with a question, which is a follow up to the previous comment, this still classifies into "Information" as the main purpose of this comment is to provide information of character damage. |
| Question    | A post that primarily seeks information, clarification, advice, or recommendations from other community members. | Example 1: <br />"Help meeee huhu. C6 Diona or C3 Charlotte for Skirk?? I'm running Skirk, Yelan, and Furina and I need a healer but don't have Escoffier. Who  should I pick and what artifacts and weapon??"<br /><br />Example 2: <br />"what exact stats do i need on my navia echoing woods set? would really appreciate it if someone told me the details like the main and sub stats needed for every piece" | "My guess would be Xingqiu, Xiangling, Barbara (or any healer), Bennet/Sucrose/Fischl<br/Are you able to share what characters you have? "<br />Though comment starts with a tentative recommendation and follows by a question, this would be classify into "Question" because the main purpose of this comment is to gather information from the other user. |

**Hard edge cases:** 

1. Simple Reactions:  short comments like "thanks", "cool", emojis, memes, etc.
   - These will be classified into "Opinion" because they are a very small percentage of the dataset, which is not worth it to have another category for them. They are not informative, not argumentative, and not questions. The closest category would be "Opinion" since reactions are generally personal, which aligns with opinions being subjective and based on personal viewpoints.
2. Agreements: short comments "I agree", "you are right", etc.
   - "Opinion" for reasons similar as above.  These comments do not provide information, seek answers, or have a argument. They are phrases of personal sentiment and therefore from subjective viewpoints.

**Boundary Posts (AI generated, not actual examples in dataset)**:

| #    | Boundary               | Post                                                         | Tension                                                      | Label (Human Review) | Reasoning (Human Review)                                     |
| ---- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ |
| 1    | Analysis ↔ Opinion     | "Honestly Raiden is just better than Yae here. Her burst uptime is way smoother and the energy regen carries the whole team. Yae feels clunky in comparison." | Sounds like reasoning ("burst uptime," "energy regen") but it's vague assertion with no numbers or concrete comparison — closer to dressed-up preference. | Opinion              | No numbers or specific evidence to back up claims like "smoother uptime" and "feels clunky" |
| 2    | Analysis ↔ Information | "Furina scales off max HP, not ATK, so stacking HP% sands/goblet is correct. With ~30k HP she's pumping out solid Fanfare stacks for the team's dmg buff." | First sentence is a game fact (Information); the second applies it to a build recommendation (Analysis). Which is the main purpose? | Analysis             | Numbers, stats, and skill description to back up claims      |
| 3    | Opinion ↔ Question     | "Skirk or Neuvillette for my main DPS? I just feel like Skirk is more fun but idk if she's worth it tbh." | Expresses preference ("more fun") but the core ask is a recommendation request. | Question             | Main purpose is to ask for recommendation of main DPS        |
| 4    | Information ↔ Question | "I think the Cinder City set needs you to trigger a Nightsoul reaction to get the 4pc bonus, right? Can someone confirm?" | Provides a factual claim, but frames it as seeking confirmation. | Question             | Main purpose is to ask other users to confirm the claim, not making the claim |
| 5    | Analysis ↔ Question    | "Wouldn't running Bennett over Xiangling here lose too much pyro application for the Vape team though? Seems like the ICD would mess up the rotation." | Reads as analytical reasoning, but it's phrased as a question challenging a prior suggestion. | Question             | Main purpose is to ask other users' opinions, not making a firm statement on the character comparison |
| 6    | Opinion ↔ Information  | "Mona's the best hydro support imo, her omen burst is a 60% dmg amplify which is just insane." | "best... imo" is opinion, but the justification ("60% dmg amplify") is a hard game fact. | Opinion              | The main message is stating their preference of Mona as the best hydro support, not providing info of Mona's stats |
| 7    | Analysis ↔ Opinion     | "Go C6 Diona over C3 Charlotte. Diona's shield + heal is more consistent for Skirk, and Charlotte's healing is too tied to her field time which fights for energy. Charlotte's nice but not for this team." | Has real comparative reasoning (Analysis) but also bare preference ("nice but not for this team"). Mostly reasoned. | Analysis             | A reasonable recommendation backed up by solid reasoning. The claim of Diona over Charlotte is a conclusion from the analytical comparison, rather than a personal preference |
| 8    | Question ↔ Opinion     | "Is it just me or is Sucrose kinda useless now? Feels like every team prefers Kazuha. What do you all think?" | Phrased as a question but really fishing for agreement on a personal judgment. | Question             | The main purpose is seeking other people's agreement on their opinion, not simply expressing the opinion |




### Data Collection

One thread is chosen randomly as the source for examples. Each thread has over hundreds of comments, since each thread under this megathread section are time-based (monthly) instead of topic based, the distribution of labels is expected to be similar across different threads. All comments under the chosen thread are exported into `csv` file using an external exporter.

Example Data Source:
1. [Weekly Team/Character Building Megathread - June 2026](https://www.reddit.com/r/Genshin_Impact/comments/1u1x90u/weekly_teamcharacter_building_megathread_june/)
2. [Weekly Team/Character Building Megathread - June 2024](https://www.reddit.com/r/Genshin_Impact/comments/1d8j0m0/weekly_teamcharacter_building_megathread_june_5th/)

Tool: [Reddit Exporter](https://chromewebstore.google.com/detail/reddit-exporter/lnblpminojaaelpbaijpgpdkijkobcge)

The number of examples per label will be determined after collecting and annotating the dataset. The labels are not expected to be evenly distributed, as different discourse types occur at different frequencies within a discussion thread. It is difficult to estimate the exact number of examples per label in advance. It is acceptable that some labels may naturally have more examples than others, as this distribution can reflect the typical discourse patterns of the community.

If a label is significantly underrepresented after annotation (maybe less than 10 out of 200), I will evaluate whether there are enough examples to support meaningful classification. If necessary, I may collect additional examples from another randomly chosen thread.

Out of 299 records in the example dataset #1:

| Label       | Count | % of total |
| ----------- | ----- | ---------- |
| Question    | 118   | 39.5%      |
| Analysis    | 93    | 31.1%      |
| Opinion     | 70    | 23.4%      |
| Information | 18    | 6.0%       |

The 'Information' section is under-represented, therefore, example thread #2 is pulled in to add more examples for those label. 

Out of 588 labeled records in example dataset #2 (31 `[deleted]`/`[removed]` posts excluded):

| Label       | Count | % of total |
| ----------- | ----- | ---------- |
| Question    | 222   | 37.8%      |
| Analysis    | 222   | 37.8%      |
| Opinion     | 130   | 22.1%      |
| Information | 14    | 2.4%       |

For a balanced dataset, the final dataset is created by randomly choosing examples from each label of the two datasets. This random process is done by AI. The ratio posts for each label is pre-determined.

Out of 200 records in the final balanced dataset:

| Label       | Count | % of total |
| ----------- | ----- | ---------- |
| Question    | 60    | 30.0%      |
| Analysis    | 60    | 30.0%      |
| Opinion     | 50    | 25.0%      |
| Information | 30    | 15.0%      |


## AI Usage

1. I gave Claude my definition of the labels and asked it to generate the Boundary Posts. I reviewed the posts, manually chose a label for these posts, and recorded my reasoning

2. I gave Claude my taxonomy section and asked it to pre label the datasets. The AI-generated labels are in `pre_label` column of the data files. I copied the `pre_label` column into the `label` column, and updated the labels manually if needed.

3. I gave Claude my collected dataset and asked it to create a balanced dataset, as I realized that one of the label is under-represented. See details above in the Data Collection section.


## Spec Reflection

**One way the specs helped**: defining the label definitions as the first step was very helpful. It was pretty much foundational for all the following steps. It was a necessary spec session for both human implementation and as context for AI tools

**One way the specs diverged**: originally only one reddit thread was pulled in as data source, however, one label ended up being under-represented and more data had to be pulled in. It was written in the specs that "maybe 10 out 200 then I will pull in more data". The initial thread had just above that bar, so I decided that more data was needed to provide more samples for the "Information" label. I also thought of merging "Information" into "Analysis", but much more work would have to be done.