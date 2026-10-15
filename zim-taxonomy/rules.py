"""Taxonomy v1 and classification rules for Kiwix ZIM families.

A "family" is a ZIM name with its language code replaced by '*'
(e.g. wikipedia_*_chemistry). Rules are looked up in order:
FAMILY (exact family key) > SERIES (prefix + suffix function) > SITE (first token).
"""
import json
from pathlib import Path


# categories and their English labels come from the reference data
_REF = Path(__file__).resolve().parent.parent / "categories"
_EN = json.loads((_REF / "i18n" / "en.json").read_text())
TAXONOMY = {c["id"]: _EN[f"category-{c['id']}"]
            for c in json.loads((_REF / "categories.json").read_text())["categories"]}

# first token of the ZIM name -> categories
SITE = {}
def _site(cats, names):
    for n in names.split():
        SITE[n] = cats

_site(["encyclopedias-general-reference"], """citizendium.org marefa hamichlol kiwix.ecured klexikon vikidia
    theworldfactbook wikiquote cheatography.com""")
_site(["languages-dictionaries"], """wiktionary dicoado.org chinese.stackexchange.com conlang.stackexchange.com
    ell.stackexchange.com english.stackexchange.com esperanto.stackexchange.com
    french.stackexchange.com german.stackexchange.com italian.stackexchange.com
    japanese.stackexchange.com korean.stackexchange.com languagelearning.stackexchange.com
    latin.stackexchange.com linguistics.stackexchange.com portuguese.stackexchange.com
    rus.stackexchange.com russian.stackexchange.com spanish.stackexchange.com
    ukrainian.stackexchange.com francais-avec-pierre test-delf-dalf zaya-english-duniya-marathi
    voa""")
_site(["books-literature"], """wikisource bnr bouquineux.com africanstorybook.org booksdash prunelle
    editions-ganndal lilote litterature-audio-poetry literature.stackexchange.com
    writing.stackexchange.com ebooks.stackexchange.com athena ncert-audiobooks folgerpedia.folger.edu""")
_site(["courses-textbooks"], """wikibooks wikiversity khanacademy avanti maitre moldova-ministry-education
    diksha-std10ssc diksha-std5ssc dse youscribe eleda.education media-eleda.ouvaton.org
    education-et-numerique les-fondamentaux ghana-bece-past-questions oer4schools edutechwiki
    academia.stackexchange.com cseducators.stackexchange.com matheducators.stackexchange.com
    metakgp crashcourse ubongo milneopentextbooks.org phzh plume-app.co wikimooc""")
_site(["science-mathematics"], """apod.nasa.gov astronomy.stackexchange.com bioacoustics.stackexchange.com
    bioinformatics.stackexchange.com biology.stackexchange.com chemistry.stackexchange.com
    earthscience.stackexchange.com math.stackexchange.com mathoverflow.net physics.stackexchange.com
    hsm.stackexchange.com mattermodeling.stackexchange.com or.stackexchange.com
    proofassistants.stackexchange.com psychology.stackexchange.com space.stackexchange.com
    stats.stackexchange.com scicomp.stackexchange.com planetmath.org proofwiki.org proofwiki
    stacks.math.columbia.edu wikispecies artofproblemsolving la-chaine-de-maths-et-tiques micmaths
    matrix67.com biologie-tout-compris biologycourses dirtybiology genomicseducation
    science-in-the-bath universcience-tv astrolabe e-penser bibnum encyclopedie-environnement.org
    ethanweed learningstatistics learningstatisticswithr.com lost-stats.github.io mspeekenbrink
    ncase.me phet mooc-energie-climat puzzling.stackexchange.com""")
_site(["computers-technology"], """devdocs freecodecamp coreyms alpinelinux archlinux gentoo installgentoo
    doc.ubuntu-fr.org ubuntuusers docs.python.org peps.python dart.dev devhints.io getbootstrap.com
    gobyexample.com htdp.org jeffe.cs.illinois.edu kris-occhipinti lesscss.org lua.org mediawiki
    noted.lol opendatastructures.org openwrt.org openzim php.net postmarketos python-class-vc
    scalewaywebinars scratch-wiki techbase.kde.org termux thalesdoc unine.ch unrealircd
    www.mankier.com wikitech cloudflare.com neos-wiki permacomputing.net www.solidarite-numerique.fr
    thaki-unlocks deus-ex-silicium bitcoin
    3dprinting.stackexchange.com ai.stackexchange.com android.stackexchange.com apple.stackexchange.com
    arduino.stackexchange.com askubuntu.com bitcoin.stackexchange.com blender.stackexchange.com
    cardano.stackexchange.com civicrm.stackexchange.com codegolf.stackexchange.com
    codereview.stackexchange.com computergraphics.stackexchange.com craftcms.stackexchange.com
    crypto.stackexchange.com cs.stackexchange.com cstheory.stackexchange.com
    datascience.stackexchange.com dba.stackexchange.com devops.stackexchange.com
    drupal.stackexchange.com dsp.stackexchange.com elementaryos.stackexchange.com
    emacs.stackexchange.com eosio.stackexchange.com es.stackoverflow.com ethereum.stackexchange.com
    expressionengine.stackexchange.com gamedev.stackexchange.com genai.stackexchange.com
    gis.stackexchange.com hardwarerecs.stackexchange.com iot.stackexchange.com iota.stackexchange.com
    ja.stackoverflow.com joomla.stackexchange.com langdev.stackexchange.com magento.stackexchange.com
    mathematica.stackexchange.com monero.stackexchange.com networkengineering.stackexchange.com
    opendata.stackexchange.com opensource.stackexchange.com pt.stackoverflow.com
    quantumcomputing.stackexchange.com raspberrypi.stackexchange.com retrocomputing.stackexchange.com
    reverseengineering.stackexchange.com robotics.stackexchange.com ru.stackoverflow.com
    salesforce.stackexchange.com security.stackexchange.com serverfault.com
    sharepoint.stackexchange.com sitecore.stackexchange.com softwareengineering.stackexchange.com
    softwarerecs.stackexchange.com solana.stackexchange.com sqa.stackexchange.com stackapps.com
    stackoverflow.com stellar.stackexchange.com substrate.stackexchange.com superuser.com
    tex.stackexchange.com tezos.stackexchange.com tor.stackexchange.com unix.stackexchange.com
    ux.stackexchange.com vi.stackexchange.com webapps.stackexchange.com webmasters.stackexchange.com
    wordpress.stackexchange.com electronics.stackexchange.com ham.stackexchange.com
    engineering.stackexchange.com drones.stackexchange.com""")
_site(["health-medicine"], """mdwiki medlineplus.gov nhs.uk wikem librepathology wikiskripta wikivet.net
    medicalsciences.stackexchange.com fitness.stackexchange.com quickguidesformedicine
    skin-of-color-society hygiene-mentale""")
_site(["history"], """history.stackexchange.com nota-bene womenshistory.si.edu
    genealogy.stackexchange.com gramps-project.org""")
_site(["geography-maps-travel"], """maps wikivoyage travel.stackexchange.com expatriates.stackexchange.com
    wwwnc.cdc.gov openstreetmap-wiki mali-pour-les-nuls sh1.org aviation.stackexchange.com""")
_site(["society-politics-economy"], """economics.stackexchange.com politics.stackexchange.com law.stackexchange.com
    patents.stackexchange.com money.stackexchange.com quant.stackexchange.com bogleheads finiki
    freelancing.stackexchange.com workplace.stackexchange.com pm.stackexchange.com
    communitybuilding.stackexchange.com interpersonal.stackexchange.com citizensinformation.ie
    consumerrights.wiki hra-news.org iranwire-com radiozamaneh-com marxists.org lgbtqia.wiki
    wiki-africa cyborganthropology.com project-fuel armypubs""")
_site(["religion-philosophy"], """shamela.ws chabadpedia chabadtext yeshiva wikishia gotquestions.org liberius.net
    buddhism.stackexchange.com christianity.stackexchange.com hermeneutics.stackexchange.com
    hinduism.stackexchange.com islam.stackexchange.com judaism.stackexchange.com
    philosophy.stackexchange.com internet-encyclopedia-philosophy mythology.stackexchange.com
    psiram rationalwiki skeptics.stackexchange.com""")
_site(["arts-music-film"], """breizhpartitions celticscores.com partituras-gratis.es chopin.lib.uchicago.edu
    mutopiaproject.org music.dalitio.de openmusictheory.com ragajunglism.org tomlehrersongs.com
    tonedear.com fretmap.app ibanezwiki music.stackexchange.com musicfans.stackexchange.com
    movies.stackexchange.com photo.stackexchange.com graphicdesign.stackexchange.com
    sound.stackexchange.com video.stackexchange.com studio.blender.org slam-out-loud
    anime.stackexchange.com scifi.stackexchange.com""")
_site(["games-fandom-humor"], """allthetropes alexandria.dk backrooms.fandom.com balatrowiki
    bindingofisaacrebirth bulbagarden dandwiki dwarffortresswiki.org evageeks explainxkcd
    frackinuniverse granbluefantasy inciclopedia kiwix.westeros minecraft.wiki minecraftwiki
    zh.minecraft.wiki pg3d pokemonwiki pokepedia pokewiki wikidex rimworldwiki riskofrain2
    stardewvalleywiki stupidedia survivors terraria.wiki.gg the uesp.net whitewolfwiki
    wiki.leagueoflegends.com wiki zdoom xkcd.com smbc-comics.com scientific-alliance.obscurative.ru
    boardgames.stackexchange.com chess.stackexchange.com gaming.stackexchange.com
    poker.stackexchange.com rpg.stackexchange.com worldbuilding.stackexchange.com
    bricks.stackexchange.com""")
_site(["sports-outdoors"], """sports.stackexchange.com martialarts.stackexchange.com capoeirawiki.org
    footballdatabase.com bicycles.stackexchange.com outdoors.stackexchange.com scoutwiki scoutwiki.org
    u-bourgogne.fr""")
_site(["home-food-diy"], """ifixit restarters diy.stackexchange.com woodworking.stackexchange.com
    mechanics.stackexchange.com gardening.stackexchange.com gardenology lifehacks.stackexchange.com
    parenting.stackexchange.com pets.stackexchange.com crafts.stackexchange.com mondial-tissus
    fountainpen cooking.stackexchange.com coffee.stackexchange.com alcohol.stackexchange.com
    homebrew.stackexchange.com vegetarianism.stackexchange.com based.cooking cuisinelibre.org
    kochwiki.org publicdomainrecipes.com grimgrains foss.cooking appropedia solar.lowtechmagazine.com
    energypedia ekopedia kiwix.ekopedia sustainability.stackexchange.com t4-wiki""")
_site(["survival-preparedness"], """100r.co canadian-prepper cd3wdproject.org lrnselfreliance rabbitwaves.ca
    s2underground survivorlibrary.com trueprepper.com urban-prepper usda-2015 wikiciv www.ready.gov
    zimgit-food-preparation zimgit-knots zimgit-medicine zimgit-post-disaster zimgit-water
    irp.fas.org""")
_site(["computers-technology", "survival-preparedness"], "anonymousplanet.org privacydefence.org incognitocat.me")

# exact family keys (override SITE)
FAMILY = {
    "zimgit-medicine_en": ["survival-preparedness", "health-medicine"],
    "irp.fas.org_*_military-medicine": ["survival-preparedness", "health-medicine"],
    "madrasa_*_arabic": ["languages-dictionaries"],
    "madrasa_*_poetry": ["books-literature"],
    "madrasa_*_stories": ["books-literature"],
    "madrasa_*_songs": ["arts-music-film"],
    "madrasa_*_scientists": ["science-mathematics", "history"],
    "madrasa_*_futureencyclopedia": ["computers-technology"],
    "madrasa_*_electeng": ["science-mathematics"],
    "shamela.ws_*_al-lugha": ["languages-dictionaries", "religion-philosophy"],
    "shamela.ws_*_al-balagha": ["languages-dictionaries", "religion-philosophy"],
    "shamela.ws_*_al-shir-wa-dawawinu": ["books-literature"],
    "shamela.ws_*_al-ansab": ["history"],
    "shamela.ws_*_al-buldan-wa-al-rihlat": ["geography-maps-travel", "history"],
    "shamela.ws_*_al-mantiq": ["religion-philosophy"],
    "ted_*_all": ["encyclopedias-general-reference"],
    "wikipedia_*_knots": ["home-food-diy"],
}

# series: first token -> function(suffix) -> categories
def _wikipedia(s):
    return {
        "all": ["encyclopedias-general-reference"], "top": ["encyclopedias-general-reference"], "100": ["encyclopedias-general-reference"], "top1m": ["encyclopedias-general-reference"],
        "50000": ["encyclopedias-general-reference"], "for_schools": ["encyclopedias-general-reference", "courses-textbooks"],
        "astronomy": ["science-mathematics"], "chemistry": ["science-mathematics"], "mathematics": ["science-mathematics"],
        "physics": ["science-mathematics"], "molcell": ["science-mathematics"], "climate-change": ["science-mathematics"],
        "computer": ["computers-technology"], "medicine": ["health-medicine"], "history": ["history"],
        "geography": ["geography-maps-travel"], "sociology": ["society-politics-economy"],
        "comics": ["arts-music-film"], "movies": ["arts-music-film"], "indian-cinema": ["arts-music-film"], "nollywood": ["arts-music-film"],
        "ray-charles": ["arts-music-film"],
        "baseball": ["sports-outdoors"], "basketball": ["sports-outdoors"], "cricket": ["sports-outdoors"],
        "football": ["sports-outdoors"], "golf": ["sports-outdoors"], "ice-hockey": ["sports-outdoors"], "tennis": ["sports-outdoors"],
        "tunisie": ["geography-maps-travel", "history"], "venezuela": ["geography-maps-travel", "history"],
    }.get(s)

def _gutenberg(s):
    lcc = s.removeprefix("lcc-")
    if s == "all" or lcc in ("a", "z"):
        return ["books-literature"]
    if lcc.startswith("p"):
        return ["books-literature"]
    subj = {"b": "religion-philosophy", "c": "history", "d": "history", "e": "history", "f": "history",
            "g": "geography-maps-travel", "h": "society-politics-economy", "j": "society-politics-economy", "k": "society-politics-economy", "l": "courses-textbooks",
            "m": "arts-music-film", "n": "arts-music-film", "q": "science-mathematics", "r": "health-medicine", "s": "home-food-diy",
            "t": "science-mathematics", "u": "history", "v": "history"}.get(lcc)
    return ["books-literature", subj] if subj else None

def _cps(s):
    return {"agronomie": ["science-mathematics", "home-food-diy"], "all": ["science-mathematics"], "arts": ["arts-music-film"],
            "defense": ["society-politics-economy"], "economie": ["society-politics-economy"], "geographie": ["geography-maps-travel"],
            "histoire": ["history"], "medecine": ["health-medicine"], "corps-humain": ["health-medicine"],
            "sport": ["sports-outdoors"], "technologie": ["science-mathematics"], "transports": ["science-mathematics"],
            }.get(s, ["science-mathematics"])

def _libretexts(s):
    return {"biz": ["society-politics-economy"], "human": ["books-literature", "history"], "k12": ["courses-textbooks"],
            "med": ["health-medicine"], "socialsci": ["society-politics-economy"], "workforce": ["courses-textbooks"],
            "eng": ["science-mathematics"]}.get(s, ["science-mathematics"])

TED_TOPICS = {
    "science-mathematics": """aliens anthropocene asteroid astrobiology astronomy bacteria bees big-bang biodiversity
        biology biomimicry biosphere birds botany brain chemistry climate-change cognitive-science
        consciousness conservation coral-reefs crispr dark-matter deextinction dinosaurs discovery dna
        ecology evolution exploration fish fungi genetics geology glaciers insects life marine-biology
        mars math microbes microbiology mission-blue moon nasa natural-disaster nature neurology
        neuroscience ocean paleontology physics planets plants primates psychology quantum rivers
        rocket-science science solar-system space statistics string-theory sun synthetic-biology
        telescopes time trees universe weather wildlife animals environment pollution plastic
        natural-resources water energy renewable-energy solar-energy wind-energy nuclear-energy
        fossil-fuels sustainability biotech nanotechnology engineering invention innovation
        electricity flight forensics illusion memory sound curiosity animals antarctica
        """,
    "computers-technology": """3d-printing ai algorithm augmented-reality blockchain code computers cryptocurrency
        cyber-security data drones driverless-cars encryption internet machine-learning metaverse
        nfts online-privacy robots software tech technology virtual-reality visualizations
        social-media surveillance bionics prosthetics demo manufacturing ux-design""",
    "health-medicine": """addiction aging aids alzheimers autism-spectrum-disorder blindness cancer coronavirus
        depression disease drugs ebola exercise health health-care hearing heart human-body illness
        medical-imaging medical-research medicine mental-health pain pandemic pregnancy ptsd
        public-health reproductive-health sight sleep smell suicide surgery vaccines virus tedmed
        disability body-language bioethics meditation mindfulness""",
    "history":                          "ancient-world archaeology history egypt slavery",
    "geography-maps-travel":            "africa asia brazil china europe india middle-east south-america united-states maps travel cities urban-planning transportation infrastructure",
    "society-politics-economy": """activism behavioral-economics bullying business capitalism career collaboration
        communication community competition consumerism corruption crime current-events democracy
        diversity economics entrepreneur equality feminism finance gender global-issues government
        homelessness human-rights identity immigration inclusion indigenous-peoples
        international-development international-relations investing journalism justice-system law
        leadership lgbtqia marketing media military money philanthropy policy politics poverty prison
        protest race refugees sexual-violence social-change society sociology terrorism transgender
        trust violence war women women-in-business work work-life-balance worklife youth
        anthropology culture shopping public-space interview productivity motivation success goals
        decision-making family parenting relationships love friendship sex kids emotions empathy
        compassion fear happiness personality personal-growth self vulnerability potential
        public-speaking humanity ideas future""",
    "religion-philosophy":              "atheism buddhism christianity ethics islam philosophy religion death",
    "arts-music-film": """animation architecture art beauty books comedy conducting creativity dance design
        entertainment fashion film graphic-design industrial-design library literature magic museums
        music painting performance photography poetry product-design science-fiction spoken-word
        storytelling street-art television theater tv typography writing""",
    "courses-textbooks":                   "education teaching ted-ed language grammar",
    "sports-outdoors":                  "sports play",
    "home-food-diy":                    "agriculture farming food gardening toys",
    "games-fandom-humor":               "gaming humor",
}
TED_MAP = {t: c for c, ts in TED_TOPICS.items() for t in ts.split()}

def _ted(s):
    if s in TED_MAP:
        return [TED_MAP[s]]
    if s.startswith("ted") or s in ("audacious-project", "best-of-the-web", "countdown"):
        return ["encyclopedias-general-reference"]
    return None

SERIES = {
    "wikipedia": _wikipedia, "gutenberg": _gutenberg, "cest-pas-sorcier": _cps,
    "libretexts.org": _libretexts, "ted": _ted,
}

_site(["science-mathematics"], "madrasa")
_site(["computers-technology"], "tridion.stackexchange.com wikimedia")
TED_MAP["resources"] = "science-mathematics"

# ---- v2: subject-specific courses get Courses & Textbooks too

def _maitre(s):
    s = s.removesuffix("_fr")
    lang = ("lecture grammaire conjugaison dictees ecriture confusion_des_lettres "
            "completer_les_mots").split()
    if s in lang: return ["languages-dictionaries"]
    if s == "enseignement_civique": return ["society-politics-economy"]
    if s == "apprendre_a_dessiner": return ["arts-music-film"]
    if s == "alimentation": return ["health-medicine"]
    return ["science-mathematics"]
SERIES["maitre"] = _maitre

_site(["science-mathematics"], "avanti")
_site(["languages-dictionaries"], "francais-avec-pierre test-delf-dalf plume-app.co")

# primary category comes from rules above; these ADD categories on top
ADD = {
    "courses-textbooks": """libretexts.org avanti maitre madrasa freecodecamp unine.ch python-class-vc htdp.org
        jeffe.cs.illinois.edu opendatastructures.org ethanweed learningstatistics
        learningstatisticswithr.com mspeekenbrink openmusictheory.com artofproblemsolving
        la-chaine-de-maths-et-tiques francais-avec-pierre test-delf-dalf biologycourses
        mooc-energie-climat zaya-english-duniya-marathi voa plume-app.co""",
    "for-children": """vikidia klexikon africanstorybook.org booksdash prunelle editions-ganndal lilote
        maitre ubongo eleda.education media-eleda.ouvaton.org les-fondamentaux dicoado.org
        plume-app.co slam-out-loud zaya-english-duniya-marathi diksha-std5ssc""",
}
ADD_FAMILY = {
    "wikipedia_*_for_schools": ["for-children"], "youscribe_*_primaire": ["for-children"],
    "voa_*_all": ["for-children"], "ted_*_ted-ed": [], "madrasa_*_songs": ["for-children"],
    "madrasa_*_stories": ["for-children"],
    **{f"moldova-ministry-education_*_clasa{i}": ["for-children"] for i in range(1, 5)},
}
ADD_SITE = {}
for c, ns in ADD.items():
    for n in ns.split(): ADD_SITE.setdefault(n, []).append(c)
# madrasa songs/stories/poetry aren't courses
NO_EDU = {"madrasa_*_songs", "madrasa_*_stories", "madrasa_*_poetry", "madrasa_*_futureencyclopedia",
          "libretexts.org_*_k12", "libretexts.org_*_workforce"}

# For Children counts as the 2nd category: kids school content -> children + education only
FAMILY_FINAL = {
    "voa_*_all": ["languages-dictionaries", "for-children"],
    "zaya-english-duniya-marathi_mr": ["languages-dictionaries", "for-children"],
    "plume-app.co_*_all": ["languages-dictionaries", "for-children"],
    "wikipedia_*_for_schools": ["encyclopedias-general-reference", "for-children"],
    "libretexts.org_*_human": ["courses-textbooks"],
    "madrasa_*_scientists": ["science-mathematics", "history"],
}
def finalize(key, cats):
    if key in FAMILY_FINAL: return FAMILY_FINAL[key]
    if key.startswith("maitre_"): return ["courses-textbooks", "for-children"]
    return cats
