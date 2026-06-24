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

| # | Boundary | Post | Tension | Label (Human Review) | Reasoning (Human Review) |
| --- | --- | --- | --- | --- | --- |
| 1 | Analysis ↔ Opinion | "Honestly Raiden is just better than Yae here. Her burst uptime is way smoother and the energy regen carries the whole team. Yae feels clunky in comparison." | Sounds like reasoning ("burst uptime," "energy regen") but it's vague assertion with no numbers or concrete comparison — closer to dressed-up preference. | Opinion | No numbers or specific evidence to back up claims like "smoother uptime" and "feels clunky" |
| 2 | Analysis ↔ Information | "Furina scales off max HP, not ATK, so stacking HP% sands/goblet is correct. With ~30k HP she's pumping out solid Fanfare stacks for the team's dmg buff." | First sentence is a game fact (Information); the second applies it to a build recommendation (Analysis). Which is the main purpose? | Analysis | Numbers, stats, and skill description to back up claims |
| 3 | Opinion ↔ Question | "Skirk or Neuvillette for my main DPS? I just feel like Skirk is more fun but idk if she's worth it tbh." | Expresses preference ("more fun") but the core ask is a recommendation request. | Question | Main purpose is to ask for recommendation of main DPS |
| 4 | Information ↔ Question | "I think the Cinder City set needs you to trigger a Nightsoul reaction to get the 4pc bonus, right? Can someone confirm?" | Provides a factual claim, but frames it as seeking confirmation. | Question | Main purpose is to ask other users to confirm the claim, not making the claim |
| 5 | Analysis ↔ Question | "Wouldn't running Bennett over Xiangling here lose too much pyro application for the Vape team though? Seems like the ICD would mess up the rotation." | Reads as analytical reasoning, but it's phrased as a question challenging a prior suggestion. | Question | Main purpose is to ask other users' opinions, not making a firm statement on the character comparison |
| 6 | Opinion ↔ Information | "Mona's the best hydro support imo, her omen burst is a 60% dmg amplify which is just insane." | "best... imo" is opinion, but the justification ("60% dmg amplify") is a hard game fact. | Opinion | The main message is stating their preference of Mona as the best hydro support, not providing info of Mona's stats |
| 7 | Analysis ↔ Opinion | "Go C6 Diona over C3 Charlotte. Diona's shield + heal is more consistent for Skirk, and Charlotte's healing is too tied to her field time which fights for energy. Charlotte's nice but not for this team." | Has real comparative reasoning (Analysis) but also bare preference ("nice but not for this team"). Mostly reasoned. | Analysis | A reasonable recommendation backed up by solid reasoning. The claim of Diona over Charlotte is a conclusion from the analytical comparison, rather than a personal preference |
| 8 | Question ↔ Opinion | "Is it just me or is Sucrose kinda useless now? Feels like every team prefers Kazuha. What do you all think?" | Phrased as a question but really fishing for agreement on a personal judgment. | Question | The main purpose is seeking other people's agreement on their opinion, not simply expressing the opinion |




### Data Collection

One thread is chosen randomly as the source for examples. Each thread has over hundreds of comments, since each thread under this megathread section are time-based (monthly) instead of topic based, the distribution of labels is expected to be similar across different threads. All comments under the chosen thread are exported into `csv` file using an external exporter.

Example Data Source: [Weekly Team/Character Building Megathread - June](https://www.reddit.com/r/Genshin_Impact/comments/1u1x90u/weekly_teamcharacter_building_megathread_june/)

Tool: [Reddit Exporter](https://chromewebstore.google.com/detail/reddit-exporter/lnblpminojaaelpbaijpgpdkijkobcge)

The number of examples per label will be determined after collecting and annotating the dataset. The labels are not expected to be evenly distributed, as different discourse types occur at different frequencies within a discussion thread. It is difficult to estimate the exact number of examples per label in advance. It is acceptable that some labels may naturally have more examples than others, as this distribution can reflect the typical discourse patterns of the community.

If a label is significantly underrepresented after annotation (maybe less than 10 out of 200), I will evaluate whether there are enough examples to support meaningful classification. If necessary, I may collect additional examples from another randomly chosen thread.



### Evaluation Metrics

**overall accuracy** = correct predictions ÷ total predictions

**per-class accuracy** = correct predictions for a specific label ÷ total examples of the specific label in the test set

Overall accuracy tells me how the model does on the whole dataset, but it can hide problems. Since my labels are not evenly distributed, the model could score high just by guessing the most common label while doing badly on rare ones. Per-class accuracy fixes this by showing how well each label is predicted on its own, so I can spot weak labels (for example, Analysis vs. Opinion).



### Definition of Success 

An 80% overall accuracy would make this classifier genuinely useful. On top of that, I want each label to reach at least 70% per-class accuracy, so no single label is left far behind. If both targets are met, the tool is reliable enough to help filter useful advice from opinions in a real community thread.


### AI Tool Plan

- **Label stress-testing:** I will give Claude label definition and edge case description and ask it to generate 5 - 10 posts that sit at the boundary between two labels. Then, I will review these posts, attempt to classify them, and tighten my label definitions if needed. (See Boundary Posts (AI generated) section above)

- **Annotation assistance:** I will give Claude label definition and edge case description  and ask it to pre-label a batch of examples before reviewing them myself. To track the examples labeled by AI, I will have a `pre_label` column in the data for AI to pre label. After I review the examples and finalize the labels in the `label` column, this `label` column is what will be used for fine tuning process. 
- **Failure analysis:**  I will review the misclassified examples and use Claude to help identify common patterns among the errors. I will look for recurring sources of confusion, such as overlap between Analysis and Opinion, mixed-intent posts, or ambiguous wording. I will verify the patterns by manually examining the original examples and checking whether similar mistakes actually occur consistently across the dataset.