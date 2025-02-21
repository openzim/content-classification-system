# Creating a user-centric, dynamic categorisation system for Kiwix - the KCCS (Kiwix Content Classification System)

## Aims and scope

### A quick overview (using the “STAR” framework)

**Situation —** Kiwix currently has a highly heterogeneous, format-oriented tagging system that is inefficient for supporting content discovery. 
Task—Content-oriented classification (tagging, in the technical sense) was identified as a possible solution. → Adapting and aiding the adoption of a classification system for Kiwix with a community-first approach and high emphasis on conciseness, flexibility, and extensibility.
 
**Action —** A content-oriented classification system was conceived based on currently used library classification systems, analysis of current Kiwix content, and internal feedback. Layers of necessary classification (tagging) were identified (classification, language, technical, and community tags). Based on conversations with the lead developer, [a UX system and mockup UI](./UI%20MockUp%20Jan2025.excalidraw.png) have been developed to aid the implementation. Additionally, the consultant conducted a proof-of-concept tagging of current content and tested it with a simple content distribution analysis to analyse how the new classification system behaves when applied to real-world content. 

**Result (~deliverables)**
- This document. 
- A series of GitHub issues for the development team (to be delivered - needs an additional consultation regarding the issue structure and details required).
- Classification guide
- Guidelines to create and change community tags.
- [Basic UI mockup](./UI%20MockUp%20Jan2025.excalidraw.png). 


### A look from a project management perspective

**People -** Benoît, Stephane, Attila, Community members (crowd-sourced community tags) (so far)

**Process -** Creating the classification system and tagging structure → Classification system freeze (December) → Proof of Concept - testing the system on a random sample of zims (in progress, as it leads to subtle changes to the classification system) → Classification distribution analysis - how the zims get distributed between the classification tags, longtail-like distribution expected, but ideally it should be closer to a “bell curve” around 1. Education and Reference) → UI and UX focused meeting (around secondary deliverable from consultant) → GitHub issues to aid development (into January) → Implementing suggestions from community members, acting on internal feedback → Implementation (hopefully 🙂)

**Product -** An extensible, concise categorisation system and a redesigned cross-platform browsing functionality aiding content discovery on Kiwix.

## About the proposed classification system
(WIP!)

KCCS is inspired in its heading structure by the **Library of Congress** and **Universal Decimal Classification** systems widely used in libraries. However, it **rationalises the main categories** and brings them to the 21st century. 

In the case of the KCCS, there are no empty classes or separate headings for subjects commonly considered a subfield or a larger classification unit. For example, there is no separate top-level heading for Philosophy or Mathematics. Instead, these are categorised under *Culture and Heritage*, and *Science*, respectively. 

There was an internal consensus that the system should be user-focused. As a result, it does not follow strict scientific classification or established librarianship conventions. Instead, it focuses on enhancing the user experience by **putting descriptive subject headings right in front of the user, attempting to follow real-world user needs and amplify common-sense usage patterns**. For instance, the *“3. Science & Technology”* section has a separate second-level category called *“3.2. Technology”*. Someone could argue that this could’ve been included in the *“3.3. Applied Sciences”* second-level category, possibly even in the *“3.3.1. Engineering and Architecture”* third-level category, but considering the abundance of material, the popularity and future prospects of the field, the establishment of a separate second-level category seemed justified. Compared to established classification systems, KCCS is simplified and as concise as possible. However, it still tries to be all-encompassing, just like the content Kiwix serves to its users.

Kiwix content is highly multidisciplinary, and many ZIMs can be considered reference works. Some content can be regarded as popular science, while others can be considered scientific. Except 1.1.1. Comprehensive Encyclopedias, the classification system facilitates content discovery by adding the optimal number of appropriate tags to each ZIM.

The optimal number of classification items shall be defined as such: **allow for enough coverage to make the item discoverable across various searches while avoiding excessive granularity that may complicate retrieval or overwhelm or confuse users**.

As an arbitrary guideline, the KCCS should aim for a **minimum of 1 and a maximum of 5 classification tags**.
	
- The focus is on precision and relevance rather than breadth.
- Multiple tags should only be added if the item significantly connects with different fields of study but cannot be included in 1.1.1. Comprehensive Encyclopedias.

**The key is to choose classification tags that are both highly relevant and varied enough to capture different aspects of the item’s content, audience, and context. The number of appropriate tags shall be decided by the team member responsible for ZIM classification, keeping internal and community feedback in mind.**


## Technical considerations

### Content tagging

**Classification tags -** tags from our classification system that efficiently describe our content - can be up to 5; otherwise, the content is in `1.1. Encyclopedias, Reference Works, Educational Resources & Multidisciplinary Works and General Knowledge`

**Technical tags -** tags about form and “physical” properties, like contained media and file size - one can be added from every category.

**Community tags** are crowd-sourced; they help the community reveal otherwise hidden use cases and meanings. Multiple can be added.

**Language tags -** denoting content language - multiple can be added.

**Tags allow flexible navigation, act as search filters, and enable dynamic updating as new content is added. The numbers in front of the categories only serve as unique identifiers in the metadata; they are generally hidden from the users,** and the translations of the key-translation value pairs are shown instead. So, instead of 1.1.2, the user only sees “Specialised Encyclopedias” or “Encyclopédies spécialisées,” depending on their UI language settings. *(NOTA: Changing them to Object Identifiers (OIDs) is under discussion)*

**ZIM files will be tagged with their respective category (multiple possible), subcategory (multiple possible), technical tag(s), language tag(s), and an arbitrary number of community tags for “crowd-enhanced discoverability”.**

An example: PhET Interactive Simulations are tagged with the 1.2.1. Natural Sciences, 1.1.4. Knowledge as Entertainment, 3.1.1. Mathematics, Physics, Chemistry, and Earth Sciences. Kiwix team members add the classification, language, and technical tags. Still, we cannot possibly cover all community use cases, so a **particular group of community members should have the right to add so-called “community tags”**. For example, John Appleseed is a community member aware that many people use specific PhET simulations for complex unit conversion, so he adds “unit-conversion” as a community tag. (There is no predefined dictionary for community tags. It mainly relies on community self-regulation. In true Wiki fashion, **Kiwix team members and/or trusted community members should vet community tags before becoming public.)**

### User Experience Enhancements

(compared to the current, largely format-only discovery system)

**Hierarchical, content-based browsing:** Users can explore categories via a tree structure without typing, no matter what type of device they use. This also means that they don’t need to know a search term to reach relevant content; they just need basic knowledge of the domain in which they are interested.

**Future enhancement - Search Integration:** Keyword searches linked to metadata tags for precise results and maybe even search suggestions.

**Possibility to discover subjects from multiple angles and easy cross-referencing:** Related resources are connected on the content level across categories for a seamless browsing experience.

**Extensibility** and **future-proofing**
- New categories can be added as Kiwix content grows.
- Specialized topics or interdisciplinary resources are easily discoverable.
- User-driven customisation, such as institutional or regional needs. (A topic to explore in the future - regionally customised home pages? User-aware homepages could be a thing, but they come with additional tracking needs, something Kiwix is not in the business of doing, as far as I can tell.)

**A subject-based** or **content-based** categorisation system provides a robust framework for organising Kiwix content. It prioritises user accessibility, supports discovery and exploration, and ensures scalability for future growth. The hope is by adopting this system, Kiwix can enhance its mission of making knowledge accessible to all, offline and beyond.

### Possible “dangers”, drawbacks and shortcomings

**The following possible negative effects or shortcomings of the system have been identified so far:**
- Significant development overhead for developer(s), possibly to the detriment of other development areas.
- Retroactive tagging, after the initial tagging, requires human resources and frequent interaction with the community (possibly a positive thing, as it can lead to a great collaborative effort)
- A laissez-faire approach with the community tags can lead to a chaotic landscape of tagging, with the possibility of inappropriate tags appearing on the platform (a centralised check from a content and/or community manager, or a “peer-review” system is needed before public tag availability)
- Community concerns related to the unorthodox structure of the classification system (headers not corresponding with established systems, leading to some confusion to people aware of their existence, approx. 5-10% of users)
- Leaving out or making it hard to classify a socially or politically sensitive subject
- If a serious shortcoming is identified after the initial classification, changing the system and reclassifying content can take a lot of resources. (A drawback of the precoordinated approach.)


## The proposed classification system (WIP)

```
1. Education & Reference

1.1. Encyclopedias, Reference Works, Educational Resources & Multidisciplinary Works and General Knowledge
1.1.1. Comprehensive Encyclopedias (e.g., Wikipedia)
1.1.2. Specialised Encyclopedias (e.g., Medical, Science-specific)
1.1.3. Language & Grammar (e.g., Wiktionary)
1.1.4. Knowledge as Entertainment

1.2. Academic Subjects 
1.2.1. Science (e.g., Physics, Chemistry, Biology)
1.2.2. Humanities & Social Sciences (e.g., History, Philosophy, Sociology)
1.2.3. Applied Science (e.g., Engineering, Computer Science)

1.3. Study Aids
1.3.1. Textbooks (e.g., OpenStax)
1.3.2. Exam Preparation (e.g., Practice Tests, Guides, Cheat Sheets)
1.3.3. Tutorials & How-To Guides (e.g., Wikibooks, Wikihow)
1.4 Open Access Scientific Content (DOAJ, ArXiV?, All OJS and EPrints journals through OAI-PMH?), OpenAlex?


2. Culture, Arts, & Literature

2.1. Literature
2.1.1. Classic Works (e.g., Project Gutenberg)
2.1.2. Contemporary Creative Commons Books (DOAB?)
2.1.3. Poetry & Drama Collections

2.2. Arts & Media
2.2.1. Visual Arts (e.g., Paintings, Sculpture Resources)
2.2.2. Performing Arts (e.g., Theater, Music Archives)
2.2.3. Film, Photography & Multimedia Resources

2.3. Culture & Heritage
2.3.1. World Cultures & Cultural Anthropology
2.3.2. Religion & Philosophy
2.3.3. Folklore, Myths & Legends


3. Science & Technology

3.1. Natural Sciences (We might need separate tags for the fields, but I tried to be user-centric.)
3.1.1. Mathematics, Physics, Chemistry, and Earth Sciences (e.g., Geology, Meteorology)
3.1.2. Biology and Life Science disciplines
3.1.3. Space Science, and Emerging Fields (e.g., Astronomy, Astrophysics)

3.2. Technology
3.2.1. Software & Programming (e.g., Coding Tutorials, API Resources, Linux, Open-Source Software)
3.2.2. Hardware & Devices (e.g., RaspberryPi Resources, Electronics, Robotics)
3.2.3. Emerging Technologies (e.g., AI, Quantum Computing)

3.3. Applied Sciences
3.3.1. Engineering and Architecture (e.g., Mechanical, Civil)
3.3.2. Medical & Health Technologies
3.3.3. Agriculture & Environmental Technologies


4. Health & Wellbeing

4.1. Medical Knowledge
4.1.1. Diseases & Conditions (e.g., WikiMed)
4.1.2. Treatment & Medications
4.1.3. Preventative Medicine & Public Health

4.2. Fitness & Nutrition
4.2.1. Physical Fitness & Exercise
4.2.2. Diet & Nutrition Guides
4.2.3. Mental Health Resources

4.3. Personal Wellbeing
4.3.1. Stress Management & Relaxation
4.3.2. Self-Care & Hygiene
4.3.3. Life Coaching & Personal Growth


5. History & Geography

5.1. History
5.1.1. Global History
5.1.2. Regional & National Histories
5.1.3. Historical Figures & Biographies

5.2. Geography
5.2.1. World Geography
5.2.2. Regional and Social Geography, Maps, Atlases, and Cartography (OpenStreetMaps?)
5.2.3. Geopolitical Studies

5.3. Travel & Exploration
5.3.1. Cultural Tourism
5.3.2. Natural Wonders
5.3.3. Travel Guides & Tips (Wikivoyage linked here?)


6. Practical Skills & Lifestyle

6.1. Home & Family
6.1.1. DIY Projects & Repairs (e.g., Wikihow)
6.1.2. Gardening & Landscaping
6.1.3. Parenting & Family Life
6.1.4. Survival resources

6.2. Professional Skills
6.2.1. Business & Entrepreneurship
6.2.2. Job Skills (e.g., Resumes, Interview Prep.)
6.2.3. Financial Literacy

6.3. Recreation & Hobbies
6.3.1. Gastronomy, Cooking Skills, and Recipes
6.3.2. Crafts & Creative Arts
6.3.3. Sports & Outdoor Activities


7. News, Current Affairs & Society

7.1. News & Media
7.1.1. News Archives
7.1.2. Journalism & Reporting
7.1.3. Opinion & Editorials

7.2. Social Studies
7.2.1. Sociology & Anthropology
7.2.2. Economics & Politics, and Government Resources
7.2.3. Civic Education

7.3. Global Issues
7.3.1. Environment & Climate Change
7.3.2. Human Rights & Equality
7.3.3. Peace & Conflict Studies
```


## Guide to Modifying the Kiwix Classification System

### Structural Overview

The classification system follows a three-level decimal hierarchy, which can be extended horizontally and vertically to accommodate new categories and disciplines:
- Level 1: Major categories (e.g., "1. Education & Reference")
- Level 2: Sub-categories (e.g., "1.1. Encyclopedias, Reference Works...")
- Level 3: Specific topics (e.g., "1.1.1. Comprehensive Encyclopedias")
- (Level 4 would be 1.1.1.1, and so on. - not implemented, currently probably not needed.)

### Modification Procedures

#### Adding New Elements

**Adding a Level 1 Category**

1. Identify the appropriate position in the sequence
1. Avoid shifting existing categories
1. Assign the next available number
1. Format: `N. Category Name`

Adding a new major category after `7. News, Current Affairs & Society`:

```
8. Digital Media & Communications
```

**Adding a Level 2 Sub-category**

1. Identify the parent category
2. Use the decimal format: N.M
3. Avoid shifting existing categories

Under `3. Science & Technology`:

```
3.4. Data Science
````

**Adding a Level 3 Topic**

1. Use the full decimal notation: N.M.L
1. Avoid shifting existing categories

**Under `3.4. Data Science`:

```
3.4.1. Machine Learning Resources
3.4.2. Statistical Analysis Tools
3.4.3. Big Data Technologies
````

#### Removing Elements

**Pre-removal Checklist**

- Identify all content tagged with the classification
- Plan for content redistribution
- Document cross-references
- Backup the current structure

**Level 3 Topic Removal**

1. Remove the specific entry
1. Renumber remaining topics if necessary (try to avoid this)
1. Redistribute associated content (possibly create an alias and redirect content to other tags.)

Removing `1.1.4. Knowledge as Entertainment`:

```
1.1.1. Comprehensive Encyclopedias
1.1.2. Specialised Encyclopedias
1.1.3. Language & Grammar
[1.1.4 removed, no renumbering needed if last item]
```

**Level 2 Sub-category Removal**

1. Ensure all Level 3 topics are addressed first
2. Remove the sub-category
3. Renumber subsequent sub-categories (try to avoid this)
4. Update all related cross-references

**Level 1 Category Removal (It’s unlikely this will be needed. Try to avoid this.)**

1. Address all sub-categories and topics first
2. Remove the major category
3. Renumber all subsequent categories
4. Update all documentation and references

#### Rearranging Elements (probably not needed)

**Moving Topics Within Same Sub-category**

1. Maintain the decimal structure
2. Update numbering sequentially

Before:

```
3.1.1. Mathematics
3.1.2. Physics
3.1.3. Chemistry
```

After (moving Mathematics):

```
3.1.1. Physics
3.1.2. Chemistry
3.1.3. Mathematics
````

**Moving Sub-categories**

1. Ensure proper decimal alignment
2. Update all internal references

#### Best Practices

**Content Management**

- Maintain consistent format
- Document all changes in a changelog

**Quality Control**

1. Verify decimal sequence integrity
1. Check formatting consistency
1. Validate all cross-references
1. Test content accessibility
1. Update any related indexes or search systems

#### Special Considerations

- Update any references to moved categories
- Maintain links to external resources
- Document source connections to aid recipe creation and internal knowledge transfer (add appropriate metadata about sources, if not self-explanatory, e.g., DOAJ, ArXiv, OJS OAI aggregated)

**Content Alignment**
- Ensure content matches category descriptions (main task)
- Maintain an appropriate depth of categorisation (with an aim for specificity)
- Update any related metadata (ZIM descriptions and metadata)

## A brief guide to the categories - “Classification guide”

1. Education & Reference

This section contains resources for learning, academic research, and reference materials. It caters to general audiences, students, and educators seeking comprehensive knowledge or academic-specific content. It also contains “Knowledge as Entertainment”.

1.1. Encyclopedias, Reference Works, Educational Resources & Multidisciplinary Works and General Knowledge

Broad reference materials and general knowledge works for diverse audiences.

1.1.1. Comprehensive Encyclopedias

 General encyclopedias covering a wide range of topics (e.g., Wikipedia).

1.1.2. Specialized Encyclopedias

 Encyclopedias focused on specific disciplines (e.g., medical or other discipline-specific).

1.1.3. Language & Grammar

 Dictionaries, thesauruses, grammar guides, and language resources (e.g., Wiktionary).

1.1.4. Knowledge as Entertainment

 Trivia, fun facts, and general interest knowledge collections.

1.2. Academic Subjects

Resources are organised by academic discipline for students and professionals.

1.2.1. Science

 Content covering physics, biology, chemistry, and related scientific fields.

1.2.2. Humanities & Social Sciences

 Resources for history, philosophy, sociology, and other humanities disciplines.

1.2.3. Applied Science

 Practical applications of science, such as engineering and medicine.

1.3. Study Aids

Tools and resources designed to assist with learning and academic preparation.

1.3.1. Textbooks

 Open-access academic books (e.g., OpenStax).

1.3.2. Exam Preparation

 Practice exams, study guides, and cheat sheets.

1.3.3. Tutorials & How-To Guides

 Step-by-step instructional resources (e.g., WikiHow).

1.4. Open Access Scientific Content

Scholarly resources such as open-access journals, articles, and databases (e.g., DOAJ, ArXiv). It can include Open datasets.

2. Culture, Arts, & Literature

Covers creative expression, cultural heritage, and literary works. Designed for cultural enrichment and artistic exploration.

2.1. Literature

Collections of written works, including public domain and modern literature.

2.1.1. Classic Works

 Public domain books and classic literature (e.g., Project Gutenberg).

2.1.2. Contemporary Creative Commons Books

 Modern books released under open licenses (e.g., DOAB).

2.1.3. Poetry & Drama Collections

 Anthologies of poetry and theatrical works.

2.2. Arts & Media

Resources on visual arts, performing arts, and multimedia content.

2.2.1. Visual Arts

 Information on paintings, sculptures, and other visual art forms.

2.2.2. Performing Arts

 Archives and guides related to theatre, music, and dance.

2.2.3. Film, Photography & Multimedia Resources

 Resources on film studies, photography guides and techniques, and multimedia.

2.3. Culture & Heritage

Materials exploring global cultures, traditions, and philosophical works.

2.3.1. World Cultures & Cultural Anthropology

 Cultural studies and anthropological insights.

2.3.2. Religion & Philosophy

 Texts on religious beliefs, traditions, and philosophical thought.

2.3.3. Folklore, Myths & Legends

 Traditional stories, myths, and folklore from various cultures.

3. Science & Technology

Focused on natural and applied sciences, engineering, and emerging technologies.

3.1. Natural Sciences

Foundational sciences and cutting-edge fields of study.

3.1.1. Mathematics, Physics, Chemistry, and Earth Sciences

 Core disciplines of natural science, including geology and meteorology.

3.1.2. Biology and Life Sciences

 Resources on organisms, ecosystems, and health sciences.

3.1.3. Space Science and Emerging Fields

 Astronomy, astrophysics, and futuristic scientific fields.

3.2. Technology

Resources on programming, hardware, and cutting-edge technologies.

3.2.1. Software & Programming

 Coding tutorials, open-source software guides, and APIs.

3.2.2. Hardware & Devices

 Materials on electronics, robotics, and devices like Raspberry Pi.

3.2.3. Emerging Technologies

 AI, quantum computing, and other frontier tech.

3.3. Applied Sciences

Disciplines applying science to real-world problems.

3.3.1. Engineering and Architecture

 Mechanical, civil, and structural design content.

3.3.2. Medical & Health Technologies

 Innovations in healthcare and medical tools.

3.3.3. Agriculture & Environmental Technologies

 Sustainable practices and agricultural technologies.

4. Health & Wellbeing

Resources on physical and mental health, fitness, and personal development.

4.1. Medical Knowledge

Information on diseases, treatments, and public health.

4.1.1. Diseases & Conditions

 Databases like WikiMed with medical insights.

4.1.2. Treatment & Medications

 Guides to therapies and pharmaceuticals.

4.1.3. Preventative Medicine & Public Health

 Resources on staying healthy and preventing disease.

4.2. Fitness & Nutrition

Tools and guides for physical and dietary health.

4.2.1. Physical Fitness & Exercise

 Workout plans and fitness guides.

4.2.2. Diet & Nutrition Guides

 Meal plans, nutritional advice, and dietary tips.

4.2.3. Mental Health Resources

 Tools and practices for improving mental well-being.

4.3. Personal Wellbeing

Resources for relaxation, self-care, and life improvement.

4.3.1. Stress Management & Relaxation

 Techniques like mindfulness and relaxation techniques.

4.3.2. Self-Care & Hygiene

 Guides for personal grooming and self-care practices.

4.3.3. Life Coaching & Personal Growth

 Motivational strategies for personal improvement.

5. History & Geography

This section encompasses historical events, geographical knowledge, and travel resources for learners, researchers, and explorers.

5.1. History

Chronological and regional studies of the past and biographical works.

5.1.1. Global History

 Overviews of world history and significant global events.

5.1.2. Regional & National Histories

 Historical accounts specific to countries and regions.

5.1.3. Historical Figures & Biographies

 Profiles of influential individuals from history.

5.2. Geography

Geographical studies, maps, and regional analyses.

5.2.1. World Geography

 Global overviews of physical and human geography.

5.2.2. Regional and Social Geography, Maps, Atlases, and Cartography

 Detailed maps, atlases, and cartographic resources.

5.2.3. Geopolitical Studies

 Resources on international relations and geopolitics.

5.3. Travel & Exploration

Guides and content for adventurers and cultural enthusiasts.

5.3.1. Cultural Tourism

 Resources highlighting the cultural richness of destinations.

5.3.2. Natural Wonders

 Information on famous natural landmarks and phenomena.

5.3.3. Travel Guides & Tips

 Practical advice for travellers and explorers.

6. Practical Skills & Lifestyle

Practical resources for daily living, professional development, and leisure activities.

6.1. Home & Family

Guides on managing households and family life.

6.1.1. DIY Projects & Repairs

 Step-by-step guides for home maintenance (e.g., WikiHow).

6.1.2. Gardening & Landscaping

 Resources on plant care and landscape design. Practical botany.

6.1.3. Parenting & Family Life

 Tips and strategies for raising children and fostering family bonds.

6.1.4. Survival Resources

 Guides for emergency preparedness and survival skills.

6.2. Professional Skills

Resources for career advancement and financial literacy.

6.2.1. Business & Entrepreneurship

 Guides on starting and managing businesses.

6.2.2. Job Skills

 Resources on resumes, interviews, and workplace skills.

6.2.3. Financial Literacy

 Content on budgeting, investments, and personal finance.

6.3. Recreation & Hobbies

Resources on leisure activities and hobbies.

6.3.1. Gastronomy, Cooking Skills, and Recipes

 Cooking techniques, recipes, and food culture.

6.3.2. Crafts & Creative Arts

 DIY crafts and artistic pursuits for recreation.

6.3.3. Sports & Outdoor Activities

 Resources on various sports and outdoor hobbies.

7. News, Current Affairs & Society

Content related to current events, social issues, and societal studies.

7.1. News & Media

Archives and analysis of news and journalistic works.

7.1.1. News Archives

 Historical records of news articles and reports.

7.1.2. Journalism & Reporting

 Resources on journalistic practices and ethics.

7.1.3. Opinion & Editorials

 Collections of opinion pieces and editorials.

7.2. Social Studies

Analytical resources on society and its structures.

7.2.1. Sociology & Anthropology

 Studies on societal behaviour and human cultures.

7.2.2. Economics & Politics, and Government Resources

 Resources on political systems, economies, and governance.

7.2.3. Civic Education

 Document empowering citizens to participate in democratic processes. Applied law, government-related documents and media, and public service.

7.3. Global Issues

Resources addressing significant international challenges and topics.

7.3.1. Environment & Climate Change

 Content on ecological issues and sustainability.

7.3.2. Human Rights & Equality

 Resources on social justice and equality movements.

7.3.3. Peace & Conflict Studies

 Analysis and resources on conflict resolution and peacebuilding.

## Community Tag Uniformisation and Moderation Policy

### Purpose

**To maintain a clean, organised, and efficient tagging system that improves content discoverability and user experience. This protocol ensures consistency in the format, relevance, and management of user-generated tags, also known as community tags.**

### Guidelines for Creating Tags

#### A. General Formatting Rules

**Case Sensitivity:**
All tags must be in lowercase (e.g., `artificial intelligence`, not `Artificial Intelligence`).

**Language:**
Tags should be in the platform's primary language. If multilingual tagging is allowed, tags must be language-specific (e.g., `python-programming` for English, `programmation-python` for French).

**Length:**
Avoid excessively long tags. Ideal tags are between 2 and 4 words. (e.g., `data science`, not a `very detailed description of data science`).

**Punctuation:**
Use hyphens (-) to separate words instead of spaces, underscores, or special characters (e.g., `machine-learning`, not `machine learning` or `machine_learning`).

**No Redundancy:**
Do not create multiple tags for the same concept (e.g., `ai`, `artificial-intelligence`, and `ai-research` should be standardised to `artificial-intelligence`).

**Avoid Special Characters:**
Tags should not contain symbols, numbers (unless essential), or emojis (e.g., `web-3` is acceptable if it references a technology, but `cats🐱` is not).

#### B. Relevance and Specificity

**Be Specific:**
Tags should focus on a single concept or category (e.g., `mobile-development` rather than just `development`).

**Avoid Generic Tags:**
Overly broad terms like `interesting`, `helpful`, or `miscellaneous` are not allowed.

**Context Matters:**
Tags must be directly relevant to the content they describe. Irrelevant tags dilute the system's effectiveness.

**Avoid Personal or Temporal References:**
Do not use tags like `my-favorites`, `2025`, or `current-issues`.


### 3. Guidelines for Reviewing and Moderating “Community” or “Crowd-Sourced” Tags

#### A. Moderators’ Responsibilities

**Merging Tags:**
Consolidate redundant tags into a single, accepted format (e.g., merge `ai`, `ai-research`, and `artificial-intelligence` into `artificial-intelligence`).

**Deleting Irrelevant Tags:**
Remove vulgar, offensive, irrelevant, spammy, or too vague tags.

**Approving New Tags:**
Only approve new tags that align with this policy and fill a genuine gap in the tagging system.

#### B. Possible future tools for moderation

**Tag Dictionary:**
Create a central dictionary of pre-approved tags for common topics. Use it to guide users and moderators.

**Community Tag Uniformization ProtocolTag Suggestion:**
Implement an auto-suggestion feature to help users select existing tags instead of creating new ones. Provide clear, user-friendly instructions on tagging when users create or edit content.

**Tag Synonyms:**
Define synonyms or aliases in the system. For example, queries for ai should automatically redirect to `artificial-intelligence`.

### 4. Ongoing Maintenance
- The content manager should conduct quarterly reviews to identify and address inconsistencies in the tag database.
- Gather user feedback on the tagging system to refine the protocol. Allow trusted users to flag inappropriate or redundant tags for moderators to review.
- Keep this policy up to date with evolving platform needs and community practices.

### 5. Examples

| Good Tags | Bad Tags | Reason |
|--|--|--|
| `machine-learning` | `ML`, `ml-learning` | Standardised to one the predefined format. |
| `data-visualization` | `dataviz`, `charts` | More descriptive and precise, avoids using word fragments. |
| `climate-change` | `environment` | Relevant and specific to the topic. |

## Future work needed

Internationalisation guidelines and OID-based standardisation of tags
Glossary
