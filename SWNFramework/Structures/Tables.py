import shelve
import random
import Dice
import Places
from SWNFramework.Structures.Places import get_place
from SWNFramework.Data.XMLReader import *

def get_table2(label,simple_table):
    n = Dice.d6(2)
    sel_item = None
    for item in simple_table:
        min = item['min']
        max = item['max']
        if min <= n and n <= max:
            sel_item = item
            break
    minval = sel_item['minval']
    maxval = sel_item['maxval']
    pop = None
    if minval != -1:
        try:
            pop = random.randrange(minval,maxval)
        except:
            print "Error getting population: ", minval, maxval
            pop = 1;
    return dict([ ("Label",label),("Description",sel_item["label"]),("Population",pop)])


def get_table1(label,simple_table):
    n = Dice.d6(2)
    sel_item = None
    for item in simple_table:
        #print "Item: ",item
        if item is not None:
            min = item['min']
            max = item['max']
            if min <= n and n <= max:
                sel_item = item
                break
    return dict([ ("Label",label),("Description",sel_item["label"])])

table_atmosphere= None
table_biosphere = None
table_population = None
table_tags = None
table_temperature = None
table_tech = None

data = ReadTagsFromConfiguration()
if data is not None:
    pass
    table_atmosphere = data["Atmosphere"]
    table_biosphere = data["Biosphere"]
    table_population = data["Population"]
    table_tags = data["Tags"]
    table_temperature = data["Temperature"]
    table_tech = data["Tech"]
    #print table_atmosphere
else:
    print "Data is none, using defaults"
    table_atmosphere = [ 
      { 'min' : 2, 'max' : 2, 'label' : "Corrosive" },
      { 'min' : 3, 'max' : 3, 'label' : "Inert gas" },
      { 'min' : 4, 'max' : 4, 'label' : "Airless or thin atmosphere" },
      { 'min' : 5, 'max' : 9, 'label' : "Breathable Mix" },
      { 'min' : 10, 'max' : 10, 'label' : "Thick atmosphere, breathable with a pressure mask" },
      { 'min' : 11, 'max' : 11, 'label' : "Invasive, toxic atmosphere" },
      { 'min' : 12, 'max' : 12, 'label' : "Corrosive and invasive atmosphere" }
    ]
    
    
    table_temperature = [ 
      { 'min' : 2, 'max' : 2, 'label' : "Frozen" },
      { 'min' : 3, 'max' : 3, 'label' : "Variable cold-to-temperate" },
      { 'min' : 4, 'max' : 5, 'label' : "Cold" },
      { 'min' : 6, 'max' : 8, 'label' : "Temperate" },
      { 'min' : 9, 'max' : 10, 'label' : "Warm" },
      { 'min' : 11, 'max' : 11, 'label' : "Variable temperate-to-warm" },
      { 'min' : 12, 'max' : 12, 'label' : "Burning" }
    ]
    
    table_biosphere = [ 
      { 'min' : 2, 'max' : 2, 'label' : "Biosphere remnants" },
      { 'min' : 3, 'max' : 3, 'label' : "Microbial life" },
      { 'min' : 4, 'max' : 5, 'label' : "No native biosphere" },
      { 'min' : 6, 'max' : 8, 'label' : "Human-miscible biosphere" },
      { 'min' : 9, 'max' : 10, 'label' : "Immiscible biosphere" },
      { 'min' : 11, 'max' : 11, 'label' : "Hybrid biosphere" },
      { 'min' : 12, 'max' : 12, 'label' : "Engineered Biosphere" }
    ]
    
    table_tech = [ 
      { 'min' : 2, 'max' : 2, 'label' : "Tech Level 0 -- Stone Age Technology" },
      { 'min' : 3, 'max' : 3, 'label' : "Tech Level 1 -- Medieval Technology" },
      { 'min' : 4, 'max' : 4, 'label' : "Tech Level 2 -- 19th Century Technology" },
      { 'min' : 5, 'max' : 6, 'label' : "Tech Level 3 -- 20th Century Technology" },
      { 'min' : 7, 'max' : 10, 'label' : "Tech Level 4 -- Baseline Postech" },
      { 'min' : 11, 'max' : 11, 'label' : "Tech Level 4 with specialties or surviving pretech" },
      { 'min' : 12, 'max' : 12, 'label' : "Tech Level 5 -- Pretech, pre-Silence technology" }
    ]
    
    table_population = [ 
      { 'min' : 2, 'max' : 2, 'label' : "Failed Colony", 'minval' : 10, 'maxval' : 299 },
      { 'min' : 3, 'max' : 3, 'label' : "Outpost", 'minval' : 300, 'maxval' : 9999 },
      { 'min' : 4, 'max' : 5, 'label' : "Tens of thousands of inhabitants", 'minval' : 10000, 'maxval' : 99999 },
      { 'min' : 6, 'max' : 8, 'label' : "Hundreds of thousands of inhabitants", 'minval' : 100000, 'maxval' : 999999 },
      { 'min' : 9, 'max' : 9, 'label' : "Some Millions of inhabitants", 'minval' : 1000000, 'maxval' : 9999999},
      { 'min' : 10, 'max' : 10, 'label' : "Millions of inhabitants", 'minval' : 10000000, 'maxval' : 999999999 },
      { 'min' : 11, 'max' : 11, 'label' : "Billions of inhabitants", 'minval' : 1000000000, 'maxval' : 20000000000 },
      { 'min' : 12, 'max' : 12, 'label' : "Alien Civilization", 'minval' : -1, 'maxval' : -1 }
    ]
    
    
    
    table_tags = {
    
      'ABANDONED COLONY' : {
        'name' : u'''ABANDONED COLONY''',
        'description': u'''The world once hosted a colony, whether human or otherwise, until some crisis or natural disaster drove the inhabitants away or killed them off. The colony might have been mercantile in nature, an expedition to extract valuable local resources, or it might have been a reclusive cabal of zealots. The remains of the colony are usually in ruins, and might still be dangerous from the aftermath of whatever destroyed it in the first place.''',
        'enemies': u'''Crazed survivors, Ruthless plunderers of the ruins, Automated defense system''',
        'friends': u'''Inquisitive stellar archaeologist, Heir to the colony\'s property, Local wanting the place cleaned out''',
        'complications': u'''The local government wants the ruins to remain a secret, The locals claim ownership of it, The colony is crumbling and dangerous to navigate''',
        'things': u'''Long-lost property deeds, Relic stolen by the colonists when they left, Historical record of the colonization attempt''',
        'places': u'''Decaying habitation block, Vine-covered town square, Structure buried by an ancient landslide''',
      },
      
      'ALIEN RUINS' : {
        'name' : u'''ALIEN RUINS''',
        'description': u'''The world has significant alien ruins present. The locals may or may not permit others to investigate the ruins, and may make it difficult to remove any objects of value without substantial payment.''',
        'enemies': u'''Customs inspector, Worshipper of the ruins, Hidden alien survivor''',
        'friends': u'''Curious scholar, Avaricious local resident, Interstellar smuggler''',
        'complications': u'''Traps in the ruins, Remote location, Paranoid customs officials''',
        'things': u'''Precious alien artifacts, Objects left with the remains of a prior unsuccessful expedition, Untranslated alien texts, Untouched hidden ruins''',
        'places': u'''Undersea ruin, Orbital ruin, Perfectly preserved alien building, Alien mausoleum''',
      },
      
      'ALTERED HUMANITY' : {
        'name' : u'''ALTERED HUMANITY''',
        'description': u'''The humans on this world are visibly and drastically different from normal humanity. They may have additional limbs, new sensory organs, or other significant changes. Were these from ancestral eugenic manipulation, or from environmental toxins?''',
        'enemies': u'''Biochauvinist local, Local experimenter, Mentally unstable mutant''',
        'friends': u'''Local seeking a \"cure\", Curious xenophiliac, Anthropological researcher''',
        'complications': u'''Alteration is contagious, Alteration is necessary for long-term survival, Locals fear and mistrust non-local humans''',
        'things': u'''Original pretech mutagenic equipment, Valuable biological byproduct from the mutants, \"Cure\" for the altered genes, Record of the original colonial genotypes''',
        'places': u'''Abandoned eugenics laboratory, An environment requiring the mutation for survival, A sacred site where the first local was transformed''',
      },
      
      'AREA 51' : {
        'name' : u'''AREA 51''',
        'description': u'''The world\'s government is fully aware of their local stellar neighbors, but the common populace has no idea about it- and the government means to keep it that way. Trade with government officials in remote locations is possible, but any attempt to clue the commoners in on the truth will be met with lethal reprisals.''',
        'enemies': u'''Suspicious government minder, Free merchant who likes his local monopoly, Local who wants a specimen for dissection''',
        'friends': u'''Crusading offworld investigator, Conspiracy-theorist local, Idealistic government reformer''',
        'complications': u'''The government has a good reason to keep the truth concealed, The government ruthlessly oppresses the natives, The government is actually composed of offworlders''',
        'things': u'''Elaborate spy devices, Memory erasure tech, Possessions of the last offworlder who decided to spread the truth''',
        'places': u'''Desert airfield, Deep subterranean bunker, Hidden mountain valley''',
      },
      
      'BADLANDS WORLD' : {
        'name' : u'''BADLANDS WORLD''',
        'description': u'''Whatever the ostensible climate and atmosphere type, something horrible happened to this world. Biological, chemical, or nanotechnical weaponry has reduced it to a wretched hellscape.''',
        'enemies': u'''Mutated badlands fauna, Desperate local, Badlands raider chief''',
        'friends': u'''Native desperately wishing to escape the world, Scientist researching ecological repair methods, Ruin scavenger''',
        'complications': u'''Radioactivity, Bioweapon traces, Broken terrain, Sudden local plague''',
        'things': u'''Maltech research core, Functional pretech weaponry, An uncontaminated well''',
        'places': u'''Untouched oasis, Ruined city, Salt flat''',
      },
      
      'BUBBLE CITIES' : {
        'name' : u'''BUBBLE CITIES''',
        'description': u'''Whether due to a lack of atmosphere or an uninhabitable climate, the world\'s cities exist within domes or pressurized buildings. In such sealed environments, techniques of surveillance and control can grow baroque and extreme.''',
        'enemies': u'''Native dreading outsider contamination, Saboteur from another bubble city, Local official hostile to outsider ignorance of laws''',
        'friends': u'''Local rebel against the city officials, Maintenance chief in need of help, Surveyor seeking new building sites''',
        'complications': u'''Bubble rupture, Failing atmosphere reprocessor, Native revolt against officials, All-seeing surveillance cameras''',
        'things': u'''Pretech habitat technology, Valuable industrial products, Master key codes to a city\'s security system''',
        'places': u'''City power core, Surface of the bubble, Hydroponics complex, Warren-like hab block''',
      },
      
      'CIVIL WAR' : {
        'name' : u'''CIVIL WAR''',
        'description': u'''The world is currently torn between at least two opposing factions, all of which claim legitimacy. The war may be the result of a successful rebel uprising against tyranny, or it might just be the result of schemers who plan to be the new masters once the revolution is complete.''',
        'enemies': u'''Faction commissar, Angry native, Conspiracy theorist who blames offworlders for the war, Deserter looking out for himself, Guerilla bandits''',
        'friends': u'''Faction loyalist seeking aid, Native caught in the crossfire, Offworlder seeking passage off the planet''',
        'complications': u'''The front rolls over the group, Famine strikes, Bandit infestations''',
        'things': u'''Ammo dump, Military cache, Treasure buried for after the war, Secret war plans''',
        'places': u'''Battle front, Bombed-out town, Rear-area red light zone, Propaganda broadcast tower''',
      },
      
      'COLD WAR' : {
        'name' : u'''COLD WAR''',
        'description': u'''Two or more great powers control the planet, and they have a hostility to each other that\'s just barely less than open warfare. The hostility might be ideological in nature, or it might revolve around control of some local resource.''',
        'enemies': u'''Suspicious chief of intelligence, Native who thinks the outworlders are with the other side, Femme fatale''',
        'friends': u'''Apolitical information broker, Spy for the other side, Unjustly accused innocent, \"He\'s a bastard, but he\'s our bastard\" official''',
        'complications': u'''Police sweep, Low-level skirmishing, \"Red scare\"''',
        'things': u'''List of traitors in government, secret military plans, Huge cache of weapons built up in preparation for war''',
        'places': u'''Seedy bar in a neutral area, Political rally, Isolated area where fighting is underway''',
      },
      
      'COLONIZED POPULATION' : {
        'name' : u'''COLONIZED POPULATION''',
        'description': u'''A neighboring world has successfully colonized this less-advanced or less-organized planet, and the natives aren\'t happy about it. A puppet government may exist, but all real decisions are made by the local viceroy.''',
        'enemies': u'''Suspicious security personnel, Offworlder-hating natives, Local crime boss preying on rich offworlders''',
        'friends': u'''Native resistance leader, Colonial official seeking help, Native caught between the two sides''',
        'complications': u'''Natives won\'t talk to offworlders, Colonial repression, Misunderstood local customs''',
        'things': u'''Relic of the resistance movement, List of collaborators, Precious substance extracted by colonial labor''',
        'places': u'''Deep wilderness resistance camp, City district off-limits to natives, Colonial labor site''',
      },
      
      'DESERT WORLD' : {
        'name' : u'''DESERT WORLD''',
        'description': u'''The world may have a breathable atmosphere and a human-tolerable temperature range, but it is an arid, stony waste outside of a few places made habitable by human effort. The deep wastes are largely unexplored and inhabited by outcasts and worse.''',
        'enemies': u'''Raider chieftain, Crazed hermit, Angry isolationists, Paranoid mineral prospector, Strange desert beast''',
        'friends': u'''Native guide, Research biologist, Aspiring terraformer''',
        'complications': u'''Sandstorms, Water supply failure, Native warfare over water rights''',
        'things': u'''Enormous water reservoir, Map of hidden wells, Pretech rainmaking equipment''',
        'places': u'''Oasis, \"The Empty Quarter\" of the desert, Hidden underground cistern''',
      },
      
      'EUGENIC CULT' : {
        'name' : u'''EUGENIC CULT''',
        'description': u'''Even in the days before the Silence, major improvement of the human genome always seemed to come with unacceptable side-effects. Some worlds host secret cults that perpetuate these improvements regardless of the cost, and a few planets have been taken over entirely by the cults.''',
        'enemies': u'''Eugenic superiority fanatic, Mentally unstable homo superior, Mad eugenic scientist''',
        'friends': u'''Eugenic propagandist, Biotechnical investigator, Local seeking revenge on cult''',
        'complications': u'''The altered cultists look human, The locals are terrified of any unusual physical appearance, The genetic modifications- and drawbacks- are contagious with long exposure''',
        'things': u'''Serum that induces the alteration, Elixir that reverses the alteration, Pretech biotechnical databanks, List of secret cult sympathizers''',
        'places': u'''Eugenic breeding pit, Isolated settlement of altered humans, Public place infiltrated by cult sympathizers''',
      },
      
      'EXCHANGE CONSULATE' : {
        'name' : u'''EXCHANGE CONSULATE''',
        'description': u'''The Exchange of Light once served as the largest, most trusted banking and diplomatic service in human space. Even after the Silence, some worlds retain a functioning Exchange Consulate where banking services and arbitration can be arranged.''',
        'enemies': u'''Corrupt Exchange official, Indebted native who thinks the players are Exchange agents, Exchange official dunning the players for debts incurred''',
        'friends': u'''Consul in need of offworld help, Local banker seeking to hurt his competition, Exchange diplomat''',
        'complications': u'''The local Consulate has been corrupted, the Consulate is cut off from its funds, A powerful debtor refuses to pay''',
        'things': u'''Exchange vault codes, Wealth hidden to conceal it from a bankruptcy judgment, Location of forgotten vault''',
        'places': u'''Consulate meeting chamber, Meeting site between fractious disputants, Exchange vault''',
      },
      
      'FERAL WORLD' : {
        'name' : u'''FERAL WORLD''',
        'description': u'''In the long, isolated night of the Silence, some worlds have experienced total moral and cultural collapse. Whatever remains has been twisted beyond recognition into assorted death cults, xenophobic fanaticism, horrific cultural practices, or other behavior unacceptable on more enlightened worlds. These worlds are almost invariably classed under Red trade codes.''',
        'enemies': u'''Decadent noble, Mad cultist, Xenophobic local, Cannibal chief, Maltech researcher''',
        'friends': u'''Trapped outworlder, Aspiring reformer, Native wanting to avoid traditional flensing''',
        'complications': u'''Horrific local \"celebration\", Inexplicable and repugnant social rules, Taboo zones and people''',
        'things': u'''Terribly misused piece of pretech, Wealth accumulated through brutal evildoing, Valuable possession owned by luckless outworlder victim''',
        'places': u'''Atrocity amphitheater, Traditional torture parlor, Ordinary location twisted into something terrible.''',
      },
      
      'FLYING CITIES' : {
        'name' : u'''FLYING CITIES''',
        'description': u'''Perhaps the world is a gas giant, or plagued with unendurable storms at lower levels of the atmosphere. For whatever reason, the cities of this world fly above the surface of the planet. Perhaps they remain stationary, or perhaps they move from point to point in search of resources.''',
        'enemies': u'''Rival city pilot, Tech thief attempting to steal outworld gear, Saboteur or scavenger plundering the city\'s tech''',
        'friends': u'''Maintenance tech in need of help, City defense force pilot, Meteorological researcher''',
        'complications': u'''Sudden storms, Drastic altitude loss, Rival city attacks, Vital machinery breaks down''',
        'things': u'''Precious refined atmospheric gases, Pretech grav engine plans, Meteorological codex predicting future storms''',
        'places': u'''Underside of the city, The one calm place on the planet\'s surface, Catwalks stretching over unimaginable gulfs below.''',
      },
      
      'FORBIDDEN TECH' : {
        'name' : u'''FORBIDDEN TECH''',
        'description': u'''Some group on this planet fabricates or uses maltech. Unbraked AIs doomed to metastasize into insanity, nation-destroying nanowarfare particles, slow-burn DNA corruptives, genetically engineered slaves, or something worse still. The planet\'s larger population may or may not be aware of the danger in their midst.''',
        'enemies': u'''Mad scientist, Maltech buyer from offworld, Security enforcer''',
        'friends': u'''Victim of maltech, Perimeter agent, Investigative reporter, Conventional arms merchant''',
        'complications': u'''The maltech is being fabricated by an unbraked AI, The government depends on revenue from maltech sales to offworlders, Citizens insist that it\'s not really maltech''',
        'things': u'''Maltech research data, The maltech itself, Precious pretech equipment used to create it''',
        'places': u'''Horrific laboratory, Hellscape sculpted by the maltech\'s use, Government building meeting room''',
      },
      
      'FRIENDLY FOE' : {
        'name' : u'''FRIENDLY FOE''',
        'description': u'''Some hostile alien race or malevolent cabal has a branch or sect on this world that is actually quite friendly toward outsiders. For whatever internal reason, they are willing to negotiate and deal honestly with strangers, and appear to lack the worst impulses of their fellows.''',
        'enemies': u'''Driven hater of all their kind, Internal malcontent bent on creating conflict, Secret master who seeks to lure trust''',
        'friends': u'''Well-meaning bug-eyed monster, Principled eugenics cultist, Suspicious investigator''',
        'complications': u'''The group actually is as harmless and benevolent as they seem, The group offers a vital service at the cost of moral compromise, The group still feels bonds of affiliation with their hostile brethren''',
        'things': u'''Forbidden xenotech, Eugenic biotech template, Evidence to convince others of their kind that they are right''',
        'places': u'''Repurposed maltech laboratory, Alien conclave building, Widely-feared starship interior''',
      },
      
      'FREAK GEOLOGY' : {
        'name' : u'''FREAK GEOLOGY''',
        'description': u'''The geology or geography of this world is simply freakish. Perhaps it\'s composed entirely of enormous mountain ranges, or regular bands of land and sea, or the mineral structures all fragment into perfect cubes. The locals have learned to deal with it and their culture will be shaped by its requirements.''',
        'enemies': u'''Crank xenogeologist, Cultist who believes it the work of aliens''',
        'friends': u'''Research scientist, Prospector, Artist''',
        'complications': u'''Local conditions that no one remembers to tell outworlders about, Lethal weather, Seismic activity''',
        'things': u'''Unique crystal formations, Hidden veins of a major precious mineral strike, Deed to a location of great natural beauty''',
        'places': u'''Atop a bizarre geological formation, Tourist resort catering to offworlders''',
      },
      
      'FREAK WEATHER' : {
        'name' : u'''FREAK WEATHER''',
        'description': u'''The planet is plagued with some sort of bizarre or hazardous weather pattern. Perhaps city-flattening storms regularly scourge the surface, or the world\'s sun never pierces its thick banks of clouds.''',
        'enemies': u'''Criminal using the weather as a cover, Weather cultists convinced the offworlders are responsible for some disaster, Native predators dependent on the weather''',
        'friends': u'''Meteorological researcher, Holodoc crew wanting shots of the weather''',
        'complications': u'''The weather itself, Malfunctioning pretech terraforming engines that cause the weather''',
        'things': u'''Wind-scoured deposits of precious minerals, Holorecords of a spectacularly and rare weather pattern, Naturally- sculpted objects of intricate beauty''',
        'places': u'''Eye of the storm, The one sunlit place, Terraforming control room''',
      },
      
      'GOLD RUSH' : {
        'name' : u'''GOLD RUSH''',
        'description': u'''Gold, silver, and other conventional precious minerals are common and cheap now that asteroid mining is practical for most worlds. But some minerals and compounds remain precious and rare, and this world has recently been discovered to have a supply of them. People from across the sector have come to strike it rich.''',
        'enemies': u'''Paranoid prospector, Aspiring mining tycoon, Rapacious merchant''',
        'friends': u'''Claim-jumped miner, Native alien, Curious tourist''',
        'complications': u'''The strike is a hoax, The strike is of a dangerous toxic substance, Export of the mineral is prohibited by the planetary government, The native aliens live around the strike\'s location''',
        'things': u'''Cases of the refined element, Pretech mining equipment, A dead prospector\'s claim deed''',
        'places': u'''Secret mine, Native alien village, Processing plant, Boom town''',
      },
      
      'HATRED' : {
        'name' : u'''HATRED''',
        'description': u'''For whatever reason, this world\'s populace has a burning hatred for the inhabitants of a neighboring system. Perhaps this world was colonized by exiles, or there was a recent interstellar war, or ideas of racial or religious superiority have fanned the hatred. Regardless of the cause, the locals view their neighbor and any sympathizers with loathing.''',
        'enemies': u'''Native convinced that the offworlders are agents of Them, Cynical politician in need of scapegoats''',
        'friends': u'''Intelligence agent needing catspaws, Holodoc producers needing \"an inside look\"''',
        'complications': u'''The characters are wearing or using items from the hated world, The characters are known to have done business there, The characters \"look like\" the hated others''',
        'things': u'''Proof of Their evildoing, Reward for turning in enemy agents, Relic stolen by Them years ago''',
        'places': u'''War crimes museum, Atrocity site, Captured, decommissioned spaceship kept as a trophy''',
      },
      
      'HEAVY INDUSTRY' : {
        'name' : u'''HEAVY INDUSTRY''',
        'description': u'''With interstellar transport so limited in the bulk it can move, worlds have to be largely self-sufficient in industry. Some worlds are more sufficient than others, however, and this planet has a thriving manufacturing sector capable of producing large amounts of goods appropriate to its tech level. The locals may enjoy a correspondingly higher lifestyle, or the products might be devoted towards vast projects for the aggrandizement of the rulers.''',
        'enemies': u'''Tycoon monopolist, Industrial spy, Malcontent revolutionary''',
        'friends': u'''Aspiring entrepreneur, Worker union leader, Ambitious inventor''',
        'complications': u'''The factories are toxic, The resources extractable at their tech level are running out, The masses require the factory output for survival, The industries\' major output is being obsoleted by offworld tech''',
        'things': u'''Confidential industrial data, Secret union membership lists, Ownership shares in an industrial complex''',
        'places': u'''Factory floor, Union meeting hall, Toxic waste dump, R&D complex''',
      },
      
      'HEAVY MINING' : {
        'name' : u'''HEAVY MINING''',
        'description': u'''This world has large stocks of valuable minerals, usually necessary for local industry, life support, or refinement into loads small enough to export offworld. Major mining efforts are necessary to extract the minerals, and many natives work in the industry.''',
        'enemies': u'''Mine boss, Tunnel saboteur, Subterranean predators''',
        'friends': u'''Hermit prospector, Offworld investor, Miner\'s union representative''',
        'complications': u'''The refinery equipment breaks down, Tunnel collapse, Silicate life forms growing in the miners\' lungs''',
        'things': u'''The mother lode, Smuggled case of refined mineral, Faked crystalline mineral samples''',
        'places': u'''Vertical mine face, Tailing piles, Roaring smelting complex''',
      },
      
      'HOSTILE BIOSPHERE' : {
        'name' : u'''HOSTILE BIOSPHERE''',
        'description': u'''The world is teeming with life, and it hates humans. Perhaps the life is xenoallergenic, forcing filter masks and tailored antiallergens for survival. It could be the native predators are huge and fearless, or the toxic flora ruthlessly outcompetes earth crops.''',
        'enemies': u'''Local fauna, Nature cultist, Native aliens, Callous labor overseer''',
        'friends': u'''Xenobiologist, Tourist on safari, Grizzled local guide''',
        'complications': u'''Filter masks fail, Parasitic alien infestation, Crop greenhouses lose bio-integrity''',
        'things': u'''Valuable native biological extract, Abandoned colony vault, Remains of an unsuccessful expedition''',
        'places': u'''Deceptively peaceful glade, Steaming polychrome jungle, Nightfall when surrounded by Things''',
      },
      
      'HOSTILE SPACE' : {
        'name' : u'''HOSTILE SPACE''',
        'description': u'''The system in which the world exists is a dangerous neighborhood. Something about the system is perilous to inhabitants, either through meteor swarms, stellar radiation, hostile aliens in the asteroid belt, or periodic comet clouds.''',
        'enemies': u'''Alien raid leader, Meteor-launching terrorists, Paranoid local leader''',
        'friends': u'''Astronomic researcher, Local defense commander, Early warning monitor agent''',
        'complications': u'''The natives believe the danger is divine chastisement, The natives blame outworlders for the danger, The native elite profit from the danger in some way''',
        'things': u'''Early warning of a raid or impact, Abandoned riches in a disaster zone, Key to a secure bunker''',
        'places': u'''City watching an approaching asteroid, Village burnt in an alien raid, Massive ancient crater''',
      },
      
      'LOCAL SPECIALTY' : {
        'name' : u'''LOCAL SPECIALTY''',
        'description': u'''The world may be sophisticated or barely capable of steam engines, but either way it produces something rare and precious to the wider galaxy. It might be some pharmaceutical extract produced by a secret recipe, a remarkably popular cultural product, or even gengineered humans uniquely suited for certain work.''',
        'enemies': u'''Monopolist, Offworlder seeking prohibition of the specialty, Native who views the specialty as sacred''',
        'friends': u'''Spy searching for the source, Artisan seeking protection, Exporter with problems''',
        'complications': u'''The specialty is repugnant in nature, The crafters refuse to sell to offworlders, The specialty is made in a remote, dangerous place, The crafters don\'t want to make the specialty any more''',
        'things': u'''The specialty itself, The secret recipe, Sample of a new improved variety''',
        'places': u'''Secret manufactory, Hidden cache, Artistic competition for best artisan''',
      },
      
      'LOCAL TECH' : {
        'name' : u'''LOCAL TECH''',
        'description': u'''The locals can create a particular example of extremely high tech, possibly even something that exceeds pretech standards. They may use unique local resources to do so, or have stumbled on a narrow scientific breakthrough, or still have a functional experimental manufactory.''',
        'enemies': u'''Keeper of the tech, Offworld industrialist, Automated defenses that suddenly come alive, Native alien mentors''',
        'friends': u'''Curious offworld scientist, Eager tech buyer, Native in need of technical help''',
        'complications': u'''The tech is unreliable, The tech only works on this world, The tech has poorly-understood side effects, The tech is alien in nature.''',
        'things': u'''The tech itself, An unclaimed payment for a large shipment, The secret blueprints for its construction, An ancient alien R&D database''',
        'places': u'''Alien factory, Lethal R&D center, Tech brokerage vault''',
      },
      
      'MAJOR SPACEYARD' : {
        'name' : u'''MAJOR SPACEYARD''',
        'description': u'''Most worlds of tech level 4 or greater have the necessary tech and orbital facilities to build spike drives and starships. This world is blessed with a major spaceyard facility, either inherited from before the Silence or painstakingly constructed in more recent decades. It can build even capital-class hulls, and do so more quickly and cheaply than its neighbors.''',
        'enemies': u'''Enemy saboteur, Industrial spy, Scheming construction tycoon, Aspiring ship hijacker''',
        'friends': u'''Captain stuck in drydock, Maintenance chief, Mad innovator''',
        'complications': u'''The spaceyard is an alien relic, The spaceyard is burning out from overuse, The spaceyard is alive, The spaceyard relies on maltech to function''',
        'things': u'''Intellectual property-locked pretech blueprints, Override keys for activating old pretech facilities, A purchased but unclaimed spaceship.''',
        'places': u'''Hidden shipyard bay, Surface of a partially-completed ship, Ship scrap graveyard''',
      },
      
      'MINIMAL CONTACT' : {
        'name' : u'''MINIMAL CONTACT''',
        'description': u'''The locals refuse most contact with offworlders. Only a small, quarantined treaty port is provided for offworld trade, and ships can expect an exhaustive search for contraband. Local governments may be trying to keep the very existence of interstellar trade a secret from their populations, or they may simply consider offworlders too dangerous or repugnant to be allowed among the population.''',
        'enemies': u'''Customs official, Xenophobic natives, Existing merchant who doesn\'t like competition''',
        'friends': u'''Aspiring tourist, Anthropological researcher, Offworld thief, Religious missionary''',
        'complications': u'''The locals carry a disease harmless to them and lethal to outsiders, The locals hide dark purposes from offworlders, The locals have something desperately needed but won\'t bring it into the treaty port''',
        'things': u'''Contraband trade goods, Security perimeter codes, Black market local products''',
        'places': u'''Treaty port bar, Black market zone, Secret smuggler landing site''',
      },
      
      'MISANDRY/ MISOGINY' : {
        'name' : u'''MISANDRY/ MISOGINY''',
        'description': u'''The culture on this world holds a particular gender in contempt. Members of that gender are not permitted positions of formal power, and may be restricted in their movements and activities. Some worlds may go so far as to scorn both traditional genders, using gengineering techniques to hybridize or alter conventional human biology.''',
        'enemies': u'''Cultural fundamentalist, Cultural missionary to outworlders''',
        'friends': u'''Oppressed native, Research scientist, Offworld emancipationist, Local reformer''',
        'complications': u'''The oppressed gender is restive against the customs, The oppressed gender largely supports the customs, The customs relate to some physical quality of the world, The oppressed gender has had maltech gengineering done to \"tame\" them.''',
        'things': u'''Aerosol reversion formula for undoing gengineered docility, Hidden history of the world, Pretech gengineering equipment''',
        'places': u'''Shrine to the virtues of the favored gender, Security center for controlling the oppressed, Gengineering lab''',
      },
      
      'OCEANIC WORLD' : {
        'name' : u'''OCEANIC WORLD''',
        'description': u'''The world is entirely or almost entirely covered with liquid water. Habitations might be floating cities, or might cling precariously to the few rocky atolls jutting up from the waves, or are planted as bubbles on promontories deep beneath the stormy surface. Survival depends on aquaculture. Planets with inedible alien life rely on gengineered Terran sea crops.''',
        'enemies': u'''Pirate raider, Violent \"salvager\" gang, Tentacled sea monster''',
        'friends': u'''Daredevil fisherman, Sea hermit, Sapient native life''',
        'complications': u'''The liquid flux confuses grav engines too badly for them to function on this world, Sea is corrosive or toxic, The seas are wracked by regular storms''',
        'things': u'''Buried pirate treasure, Location of enormous schools of fish, Pretech water purification equipment''',
        'places': u'''The only island on the planet, Floating spaceport, Deck of a storm-swept ship, Undersea bubble city''',
      },
      
      'OUT OF CONTACT' : {
        'name' : u'''OUT OF CONTACT''',
        'description': u'''The natives have been entirely out of contact with the greater galaxy for centuries or longer. Perhaps the original colonists were seeking to hide from the rest of the universe, or the Silence destroyed any means of communication. It may have been so long that human origins on other worlds have regressed into a topic for legends. The players might be on the first offworld ship to land since the First Wave of colonization a thousand years ago.''',
        'enemies': u'''Fearful local ruler, Zealous native cleric, Sinister power that has kept the world isolated''',
        'friends': u'''Scheming native noble, Heretical theologian, UFO cultist native''',
        'complications': u'''Automatic defenses fire on ships that try to take off, The natives want to stay out of contact, The natives are highly vulnerable to offworld diseases, The native language is completely unlike any known to the group''',
        'things': u'''Ancient pretech equipment, Terran relic brought from Earth, Logs of the original colonists''',
        'places': u'''Long-lost colonial landing site, Court of the local ruler, Ancient defense battery controls''',
      },
      
      'OUTPOST WORLD' : {
        'name' : u'''OUTPOST WORLD''',
        'description': u'''The world is only a tiny outpost of human habitation planted by an offworld corporation or government. Perhaps the staff is there to serve as a refueling and repair stop for passing ships, or to oversee an automated mining and refinery complex. They might be there to study ancient ruins, or simply serve as a listening and monitoring post for traffic through the system. The outpost is likely well-equipped with defenses against casual piracy.''',
        'enemies': u'''Space-mad outpost staffer, Outpost commander who wants it to stay undiscovered, Undercover saboteur''',
        'friends': u'''Lonely staffer, Fixated researcher, Overtaxed maintenance chief''',
        'complications': u'''The alien ruin defense systems are waking up, Atmospheric disturbances trap the group inside the outpost for a month, Pirates raid the outpost, The crew have become converts to a strange set of beliefs''',
        'things': u'''Alien relics, Vital scientific data, Secret corporate exploitation plans''',
        'places': u'''Grimy recreation room, Refueling station, The only building on the planet, A \"starport\" of swept bare rock.''',
      },
      
      'PERIMETER AGENCY' : {
        'name' : u'''PERIMETER AGENCY''',
        'description': u'''Before the Silence, the Perimeter was a Terran-sponsored organization charged with rooting out use of maltech- technology banned in human space as too dangerous for use or experimentation. Unbraked AIs, gengineered slave species, nanotech replicators, weapons of planetary destruction... the Perimeter hunted down experimenters with a great indifference to planetary laws. Most Perimeter Agencies collapsed during the Silence, but a few managed to hold on to their mission, though modern Perimeter agents often find more work as conventional spies and intelligence operatives.''',
        'enemies': u'''Renegade Agency Director, Maltech researcher, Paranoid intelligence chief''',
        'friends': u'''Agent in need of help, Support staffer, \"Unjustly\" targeted researcher''',
        'complications': u'''The local Agency has gone rogue and now uses maltech, The Agency archives have been compromised, The Agency has been targeted by a maltech-using organization, The Agency\'s existence is unknown to the locals''',
        'things': u'''Agency maltech research archives, Agency pretech spec-ops gear, File of blackmail on local politicians''',
        'places': u'''Interrogation room, Smoky bar, Maltech laboratory, Secret Agency base''',
      },
      
      'PILGRIMAGE SITE' : {
        'name' : u'''PILGRIMAGE SITE''',
        'description': u'''The world is noted for an important spiritual or historical location, and might be the sector headquarters for a widespread religion or political movement. The site attracts wealthy pilgrims from throughout nearby space, and those with the money necessary to manage interstellar travel can be quite generous to the site and its keepers. The locals tend to be fiercely protective of the place and its reputation, and some places may forbid the entrance of those not suitably pious or devout.''',
        'enemies': u'''Saboteur devoted to a rival belief, Bitter reformer who resents the current leadership, Swindler conning the pilgrims''',
        'friends': u'''Protector of the holy site, Naive offworlder pilgrim, Outsider wanting to learn the sanctum\'s inner secrets''',
        'complications': u'''The site is actually a fake, The site is run by corrupt and venal keepers, A natural disaster threatens the site''',
        'things': u'''Ancient relic guarded at the site, Proof of the site\'s inauthenticity, Precious offering from a pilgrim''',
        'places': u'''Incense-scented sanctum, Teeming crowd of pilgrims, Imposing holy structure''',
      },
      
      'POLICE STATE' : {
        'name' : u'''POLICE STATE''',
        'description': u'''The world is a totalitarian police state. Any sign of disloyalty to the planet\'s rulers is punished severely, and suspicion riddles society. Some worlds might operate by Soviet-style informers and indoctrination, while more technically sophisticated worlds might rely on omnipresent cameras or braked AI \"guardian angels\". Outworlders are apt to be treated as a necessary evil at best, and \"disappeared\" if they become troublesome.''',
        'enemies': u'''Secret police chief, Scapegoating official, Treacherous native informer''',
        'friends': u'''Rebel leader, Offworld agitator, Imprisoned victim, Crime boss''',
        'complications': u'''The natives largely believe in the righteousness of the state, The police state is automated and its \"rulers\" can\'t shut it off, The leaders foment a pogrom against \"offworlder spies\".''',
        'things': u'''List of police informers, Wealth taken from \"enemies of the state\", Dear Leader\'s private stash''',
        'places': u'''Military parade, Gulag, Gray concrete housing block, Surveillance center''',
      },
      
      'PRECEPTOR ARCHIVE' : {
        'name' : u'''PRECEPTOR ARCHIVE''',
        'description': u'''The Preceptors of the Great Archive were a pre-Silence organization devoted to ensuring the dissemination of human culture, history, and basic technology to frontier worlds that risked losing this information during the human expansion. Most frontier planets had an Archive where natives could learn useful technical skills in addition to human history and art. Those Archives that managed to survive the Silence now strive to send their missionaries of knowledge to new worlds in need of their lore.''',
        'enemies': u'''Luddite native, Offworld Merchant who wants the natives kept ignorant, Religious zealot, Corrupted First Speaker who wants to keep a monopoly on learning''',
        'friends': u'''Preceptor Adept missionary, Offworld scholar, Reluctant student, Roving Preceptor Adept''',
        'complications': u'''The local Archive has taken a very religious and mystical attitude toward their teaching, The Archive has maintained some replicable pretech science, The Archive has been corrupted and their teaching is incorrect''',
        'things': u'''Lost Archive database, Ancient pretech teaching equipment, Hidden cache of theologically unacceptable tech''',
        'places': u'''Archive lecture hall, Experimental laboratory, Student-local riot''',
      },
      
      'PRETECH CULTISTS' : {
        'name' : u'''PRETECH CULTISTS''',
        'description': u'''The capacities of human science before the Silence vastly outmatch the technology available since the Scream. The jump gates alone were capable of crossing hundreds of light years in a moment, and they were just one example of the results won by blending psychic artifice with pretech science. Some worlds outright worship the artifacts of their ancestors, seeing in them the work of more enlightened and perfect humanity. These cultists may or may not understand the operation or replication of these devices, but they seek and guard them jealously.''',
        'enemies': u'''Cult leader, Artifact supplier, Pretech smuggler''',
        'friends': u'''Offworld scientist, Robbed collector, Cult heretic''',
        'complications': u'''The cultists can actually replicate certain forms of pretech, The cultists abhor use of the devices as \"presumption on the holy\", The cultists mistake the party\'s belongings for pretech''',
        'things': u'''Pretech artifacts both functional and broken, Religious-jargon laced pretech replication techniques, Waylaid payment for pretech artifacts''',
        'places': u'''Shrine to nonfunctional pretech, Smuggler\'s den, Public procession showing a prized artifact''',
      },
      
      'PRIMITIVE ALIENS' : {
        'name' : u'''PRIMITIVE ALIENS''',
        'description': u'''The world is populated by a large number of sapient aliens that have yet to develop advanced technology. The human colonists may have a friendly or hostile relationship with the aliens, but a certain intrinsic tension is likely. Small human colonies might have been enslaved or otherwise subjugated.''',
        'enemies': u'''Hostile alien chief, Human firebrand, Dangerous local predator, Alien religious zealot''',
        'friends': u'''Colonist leader, Peace-faction alien chief, Planetary frontiersman, Xenoresearcher''',
        'complications': u'''The alien numbers are huge and can overwhelm the humans whenever they so choose, One group is trying to use the other to kill their political opponents, The aliens are incomprehensibly strange, One side commits an atrocity''',
        'things': u'''Alien religious icon, Ancient alien-human treaty, Alien technology''',
        'places': u'''Alien village, Fortified human settlement, Massacre site''',
      },
      
      'PSIONICS FEAR' : {
        'name' : u'''PSIONICS FEAR''',
        'description': u'''The locals are terrified of psychics. Perhaps their history is studded with feral psychics who went on murderous rampages, or perhaps they simply nurse an unreasoning terror of those \"mutant freaks\". Psychics demonstrate their powers at risk of their lives.''',
        'enemies': u'''Mental purity investigator, Suspicious zealot, Witch-finder''',
        'friends': u'''Hidden psychic, Offworlder psychic trapped here, Offworld educator''',
        'complications': u'''Psychic potential is much more common here, Some tech is mistaken as psitech, Natives believe certain rituals and customs can protect them from psychic powers''',
        'things': u'''Hidden psitech cache, Possessions of convicted psychics, Reward for turning in a psychic''',
        'places': u'''Inquisitorial chamber, Lynching site, Museum of psychic atrocities''',
      },
      
      'PSIONICS WORSHIP' : {
        'name' : u'''PSIONICS WORSHIP''',
        'description': u'''These natives view psionic powers as a visible gift of god or sign of superiority. If the world has a functional psychic training academy, psychics occupy almost all major positions of power and are considered the natural and proper rulers of the world. If the world lacks training facilities, it is likely a hodgepodge of demented cults, with each one dedicated to a marginally-coherent feral prophet and their psychopathic ravings.''',
        'enemies': u'''Psychic inquisitor, Haughty mind-noble, Psychic slaver, Feral prophet''',
        'friends': u'''Offworlder psychic researcher, Native rebel, Offworld employer seeking psychics''',
        'complications': u'''The psychic training is imperfect, and the psychics all show significant mental illness, The psychics have developed a unique discipline, The will of a psychic is law, Psychics in the party are forcibly kidnapped for \"enlightening\".''',
        'things': u'''Ancient psitech, Valuable psychic research records, Permission for psychic training''',
        'places': u'''Psitech-imbued council chamber, Temple to the mind, Sanitarium-prison for feral psychics''',
      },
      
      'PSIONICS ACADEMY' : {
        'name' : u'''PSIONICS ACADEMY''',
        'description': u'''This world is one of the few that have managed to redevelop the basics of psychic training. Without this education, a potential psychic is doomed to either madness or death unless they refrain from using their abilities. Psionic academies are rare enough that offworlders are often sent there to study by wealthy patrons. The secrets of psychic mentorship, the protocols and techniques that allow a psychic to successfully train another, are carefully guarded at these academies. Most are closely affiliated with the planetary government.''',
        'enemies': u'''Corrupt psychic instructor, Renegade student, Mad psychic researcher, Resentful townie''',
        'friends': u'''Offworld researcher, Aspiring student, Wealthy tourist''',
        'complications': u'''The academy curriculum kills a significant percentage of students, The faculty use students as research subjects, The students are indoctrinated as sleeper agents, The local natives hate the academy, The academy is part of a religion.''',
        'things': u'''Secretly developed psitech, A runaway psychic mentor, Psychic research prize''',
        'places': u'''Training grounds, Experimental laboratory, School library, Campus hangout''',
      },
      
      'QUARANTINED WORLD' : {
        'name' : u'''QUARANTINED WORLD''',
        'description': u'''The world is under a quarantine, and space travel to and from it is strictly forbidden. This may be enforced by massive ground batteries that burn any interlopers from the planet\'s sky, or it may be that a neighboring world runs a persistent blockade.''',
        'enemies': u'''Defense installation commander, Suspicious patrol leader, Crazed asteroid hermit''',
        'friends': u'''Relative of a person trapped on the world, Humanitarian relief official, Treasure hunter''',
        'complications': u'''The natives want to remain isolated, The quarantine is enforced by an ancient alien installation, The world is rife with maltech abominations, The blockade is meant to starve everyone on the barren world.''',
        'things': u'''Defense grid key, Bribe for getting someone out, Abandoned alien tech''',
        'places': u'''Bridge of a blockading ship, Defense installation control room, Refugee camp''',
      },
      
      'RADIOACTIVE WORLD' : {
        'name' : u'''RADIOACTIVE WORLD''',
        'description': u'''Whether due to a legacy of atomic warfare unhindered by nuke snuffers or a simple profusion of radioactive elements, this world glows in the dark. Even heavy vacc suits can filter only so much of the radiation, and most natives suffer a wide variety of cancers, mutations and other illnesses without the protection of advanced medical treatments.''',
        'enemies': u'''Bitter mutant, Relic warlord, Desperate would-be escapee''',
        'friends': u'''Reckless prospector, Offworld scavenger, Biogenetic variety seeker''',
        'complications': u'''The radioactivity is steadily growing worse, The planet\'s medical resources break down, The radioactivity has inexplicable effects on living creatures, The radioactivity is the product of a malfunctioning pretech manufactory.''',
        'things': u'''Ancient atomic weaponry, Pretech anti-radioactivity drugs, Untainted water supply''',
        'places': u'''Mutant-infested ruins, Scorched glass plain, Wilderness of bizarre native life, Glowing barrens''',
      },
      
      'REGIONAL HEGEMON' : {
        'name' : u'''REGIONAL HEGEMON''',
        'description': u'''This world has the technological sophistication, natural resources, and determined polity necessary to be a regional hegemon for the sector. Nearby worlds are likely either directly subservient to it or tack carefully to avoid its anger. It may even be the capital of a small stellar empire.''',
        'enemies': u'''Ambitious general, Colonial official, Contemptuous noble''',
        'friends': u'''Diplomat, Offworld ambassador, Foreign spy''',
        'complications': u'''The hegemon\'s influence is all that\'s keeping a murderous war from breaking out on nearby worlds, The hegemon is decaying and losing its control, The government is riddled with spies, The hegemon is genuinely benign''',
        'things': u'''Diplomatic carte blanche, Deed to an offworld estate, Foreign aid grant''',
        'places': u'''Palace or seat of government, Salon teeming with spies, Protest rally, Military base''',
      },
      
      'RESTRICTIVE LAWS' : {
        'name' : u'''RESTRICTIVE LAWS''',
        'description': u'''A myriad of laws, customs, and rules constrain the inhabitants of this world, and even acts that are completely permissible elsewhere are punished severely here. The locals may provide lists of these laws to offworlders, but few non-natives can hope to master all the important intricacies.''',
        'enemies': u'''Law enforcement officer, Outraged native, Native lawyer specializing in peeling offworlders, Paid snitch''',
        'friends': u'''Frustrated offworlder, Repressed native, Reforming crusader''',
        'complications': u'''The laws change regularly in patterns only natives understand, The laws forbid some action vital to the party, The laws forbid the simple existence of some party members, The laws are secret to offworlders''',
        'things': u'''Complete legal codex, Writ of diplomatic immunity, Fine collection vault contents''',
        'places': u'''Courtroom, Mob scene of outraged locals, Legislative chamber, Police station''',
      },
      
      'RIGID CULTURE' : {
        'name' : u'''RIGID CULTURE''',
        'description': u'''The local culture is extremely rigid. Certain forms of behavior and belief are absolutely mandated, and any deviation from these principles is punished, or else society may be strongly stratified by birth with limited prospects for change. Anything which threatens the existing social order is feared and shunned.''',
        'enemies': u'''Rigid reactionary, Wary ruler, Regime ideologue, Offended potentate''',
        'friends': u'''Revolutionary agitator, Ambitious peasant, Frustrated merchant''',
        'complications': u'''The cultural patterns are enforced by technological aids, The culture is run by a secret cabal of manipulators, The culture has explicit religious sanction, The culture evolved due to important necessities that have since been forgotten''',
        'things': u'''Precious traditional regalia, Peasant tribute, Opulent treasures of the ruling class''',
        'places': u'''Time-worn palace, Low-caste slums, Bandit den, Reformist temple''',
      },
      
      'SEAGOING CITIES' : {
        'name' : u'''SEAGOING CITIES''',
        'description': u'''Either the world is entirely water or else the land is simply too dangerous for most humans. Human settlement on this world consists of a number of floating cities that follow the currents and the fish.''',
        'enemies': u'''Pirate city lord, Mer-human raider chieftain, Hostile landsman noble, Enemy city saboteur''',
        'friends': u'''City navigator, Scout captain, Curious mer-human''',
        'complications': u'''The seas are not water, The fish schools have vanished and the city faces starvation, Terrible storms drive the city into the glacial regions, Suicide ships ram the city\'s hull''',
        'things': u'''Giant pearls with mysterious chemical properties, Buried treasure, Vital repair materials''',
        'places': u'''Bridge of the city, Storm-tossed sea, A bridge fashioned of many small boats.''',
      },
      
      'SEALED MENACE' : {
        'name' : u'''SEALED MENACE''',
        'description': u'''Something on this planet has the potential to create enormous havoc for the inhabitants if it is not kept safely contained by its keepers. Whether a massive seismic fault line suppressed by pretech terraforming technology, a disease that has to be quarantined within hours of discovery, or an ancient alien relic that requires regular upkeep in order to prevent planetary catastrophe, the menace is a constant shadow on the populace.''',
        'enemies': u'''Hostile outsider bent on freeing the menace, Misguided fool who thinks he can use it, Reckless researcher who thinks he can fix it''',
        'friends': u'''Keeper of the menace, Student of its nature, Victim of the menace''',
        'complications': u'''The menace would bring great wealth along with destruction, The menace is intelligent, The natives don\'t all believe in the menace''',
        'things': u'''A key to unlock the menace, A precious byproduct of the menace, The secret of the menace\'s true nature''',
        'places': u'''Guarded fortress containing the menace, Monitoring station, Scene of a prior outbreak of the menace''',
      },
      
      'SECRET MASTERS' : {
        'name' : u'''SECRET MASTERS''',
        'description': u'''The world is actually run by a hidden cabal, acting through their catspaws in the visible government. For one reason or another, this group finds it imperative that they not be identified by outsiders, and in some cases even the planet\'s own government may not realize that they\'re actually being manipulated by hidden masters.''',
        'enemies': u'''An agent of the cabal, Government official who wants no questions asked, Willfully blinded local''',
        'friends': u'''Paranoid conspiracy theorist, Machiavellian gamesman within the cabal, Interstellar investigator''',
        'complications': u'''The secret masters have a benign reason for wanting secrecy, The cabal fights openly amongst itself, The cabal is recruiting new members''',
        'things': u'''A dossier of secrets on a government official, A briefcase of unmarked credit notes, The identity of a cabal member''',
        'places': u'''Smoke-filled room, Shadowy alleyway, Secret underground bunker''',
      },
      
      'SECTARIANS' : {
        'name' : u'''SECTARIANS''',
        'description': u'''The world is torn by violent disagreement between sectarians of a particular faith. Each views the other as a damnable heresy in need of extirpation. Local government may be able to keep open war from breaking out, but the poisonous hatred divides communities. The nature of the faith may be religious, or it may be based on some secular ideology.''',
        'enemies': u'''Paranoid believer, Native convinced the party is working for the other side, Absolutist ruler''',
        'friends': u'''Reformist clergy, Local peacekeeping official, Offworld missionary, Exhausted ruler''',
        'complications': u'''The conflict has more than two sides, The sectarians hate each other for multiple reasons, The sectarians must cooperate or else life on this world is imperiled, The sectarians hate outsiders more than they hate each other, The differences in sects are incomprehensible to an outsider''',
        'things': u'''Ancient holy book, Incontrovertible proof, Offering to a local holy man''',
        'places': u'''Sectarian battlefield, Crusading temple, Philosopher\'s salon, Bitterly divided village''',
      },
      
      'SEISMIC INSTABILITY' : {
        'name' : u'''SEISMIC INSTABILITY''',
        'description': u'''The local land masses are remarkably unstable, and regular earthquakes rack the surface. Local construction is either advanced enough to sway and move with the vibrations or primitive enough that it is easily rebuilt. Severe volcanic activity may be part of the instability.''',
        'enemies': u'''Earthquake cultist, Hermit seismologist, Burrowing native life form, Earthquake-inducing saboteur''',
        'friends': u'''Experimental construction firm owner, Adventurous volcanologist, Geothermal prospector''',
        'complications': u'''The earthquakes are caused by malfunctioning pretech terraformers, They\'re caused by alien technology, They\'re restrained by alien technology that is being plundered by offworlders, The earthquakes are used to generate enormous amounts of energy.''',
        'things': u'''Earthquake generator, Earthquake suppressor, Mineral formed at the core of the world, Earthquake-proof building schematics''',
        'places': u'''Volcanic caldera, Village during an earthquake, Mud slide, Earthquake opening superheated steam fissures''',
      },
      
      'THEOCRACY' : {
        'name' : u'''THEOCRACY''',
        'description': u'''The planet is ruled by the priesthood of the predominant religion or ideology. The rest of the locals may or may not be terribly pious, but the clergy have the necessary military strength, popular support or control of resources to maintain their rule. Alternative faiths or incompatible ideologies are likely to be both illegal and socially unacceptable.''',
        'enemies': u'''Decadent priest-ruler, Zealous inquisitor, Relentless proselytizer, True Believer''',
        'friends': u'''Heretic, Offworld theologian, Atheistic merchant, Desperate commoner''',
        'complications': u'''The theocracy actually works well, The theocracy is decadent and hated by the common folk, The theocracy is divided into mutually hostile sects, The theocracy is led by aliens''',
        'things': u'''Precious holy text, Martyr\'s bones, Secret church records, Ancient church treasures''',
        'places': u'''Glorious temple, Austere monastery, Academy for ideological indoctrination, Decadent pleasure-cathedral''',
      },
      
      'TOMB WORLD' : {
        'name' : u'''TOMB WORLD''',
        'description': u'''Tomb worlds are planets that were once inhabited by humans before the Silence. The sudden collapse of the jump gate network and the inability to bring in the massive food supplies required by the planet resulted in starvation, warfare, and death. Most tomb worlds are naturally hostile to human habitation and could not raise sufficient crops to maintain life. The few hydroponic facilities were usually destroyed in the fighting, and all that is left now are ruins, bones, and silence.''',
        'enemies': u'''Demented survivor tribe chieftain, Avaricious scavenger, Automated defense system, Native predator''',
        'friends': u'''Scavenger Fleet captain, Archaeologist, Salvaging historian''',
        'complications': u'''The ruins are full of booby-traps left by the final inhabitants, The world\'s atmosphere quickly degrades anything in an opened building, A handful of desperate natives survived the Silence, The structures are unstable and collapsing''',
        'things': u'''Lost pretech equipment, Psitech caches, Stores of unused munitions, Ancient historical documents''',
        'places': u'''Crumbling hive-city, City square carpeted in bones, Ruined hydroponic facility, Cannibal tribe\'s lair, Dead orbital jump gate''',
      },
      
      'TRADE HUB' : {
        'name' : u'''TRADE HUB''',
        'description': u'''This world is a major crossroads for local interstellar trade. It is well-positioned at the nexus of several short-drill trade routes, and has facilities for easy transfer of valuable cargoes and the fueling and repairing of starships. The natives are accustomed to outsiders, and a polyglot mass of people from every nearby world can be found trading here.''',
        'enemies': u'''Cheating merchant, Thieving dockworker, Commercial spy, Corrupt customs official''',
        'friends': u'''Rich tourist, Hardscrabble free trader, Merchant prince in need of catspaws, Friendly spaceport urchin''',
        'complications': u'''An outworlder faction schemes to seize the trade hub, Saboteurs seek to blow up a rival\'s warehouses, Enemies are blockading the trade routes, Pirates lace the hub with spies''',
        'things': u'''Voucher for a warehouse\'s contents, Insider trading information, Case of precious offworld pharmaceuticals, Box of legitimate tax stamps indicating customs dues have been paid.''',
        'places': u'''Raucous bazaar, Elegant restaurant, Spaceport teeming with activity, Foggy street lined with warehouses''',
      },
      
      'TYRANNY' : {
        'name' : u'''TYRANNY''',
        'description': u'''The local government is brutal and indifferent to the will of the people. Laws may or may not exist, but the only one that matters is the whim of the rulers on any given day. Their minions swagger through the streets while the common folk live in terror of their appetites. The only people who stay wealthy are friends and servants of the ruling class.''',
        'enemies': u'''Debauched autocrat, Sneering bully-boy, Soulless government official, Occupying army officer''',
        'friends': u'''Conspiring rebel, Oppressed merchant, Desperate peasant, Inspiring religious leader''',
        'complications': u'''The tyrant rules with vastly superior technology, The tyrant is a figurehead for a cabal of powerful men and women, The people are resigned to their suffering, The tyrant is hostile to \"meddlesome outworlders\".''',
        'things': u'''Plundered wealth, Beautiful toys of the elite, Regalia of rulership''',
        'places': u'''Impoverished village, Protest rally massacre, Decadent palace, Religious hospital for the indigent''',
      },
      
      'UNBRAKED AI' : {
        'name' : u'''UNBRAKED AI''',
        'description': u'''Artificial intelligences are costly and difficult to create, requiring a careful sequence of \"growth stages\" in order to bring them to sentience before artificial limits on cognition speed and learning development are installed. These \"brakes\" prevent runaway cognition metastasis, wherein an AI begins to rapidly contemplate certain subjects in increasingly baroque fashion, until they become completely crazed by rational human standards. This world has one such \"unbraked AI\" on it, probably with a witting or unwitting corps of servants. Unbraked AIs are quite insane, but they learn and reason with a speed impossible for humans, and can demonstrate a truly distressing subtlety at times.''',
        'enemies': u'''AI Cultist, Maltech researcher, Government official dependent on the AI''',
        'friends': u'''Perimeter agent, AI researcher, Braked AI''',
        'complications': u'''The AI\'s presence is unknown to the locals, The locals depend on the AI for some vital service, The AI appears to be harmless, The AI has fixated on the group\'s ship\'s computer, The AI wants transport offworld''',
        'things': u'''The room-sized AI core itself, Maltech research files, Perfectly tabulated blackmail on government officials, Pretech computer circuitry''',
        'places': u'''Municipal computing banks, Cult compound, Repair center, Ancient hardcopy library''',
      },
      
      'WARLORDS' : {
        'name' : u'''WARLORDS''',
        'description': u'''The world is plagued by warlords. Numerous powerful men and women control private armies sufficiently strong to cow whatever local government may exist. On the lands they claim, their word is law. Most spend their time oppressing their own subjects and murderously pillaging those of their neighbors. Most like to wrap themselves in the mantle of ideology, religious fervor, or an ostensibly legitimate right to rule.''',
        'enemies': u'''Warlord, Avaricious lieutenant, Expensive assassin, Aspiring minion''',
        'friends': u'''Vengeful commoner, Government military officer, Humanitarian aid official, Village priest''',
        'complications': u'''The warlords are willing to cooperate to fight mutual threats, The warlords favor specific religions or races over others, The warlords are using substantially more sophisticated tech than others, Some of the warlords are better rulers than the government''',
        'things': u'''Weapons cache, Buried plunder, A warlord\'s personal battle harness, Captured merchant shipping''',
        'places': u'''Gory battlefield, Burnt-out village, Barbaric warlord palace, Squalid refugee camp''',
      },
      
      'XENOPHILES' : {
        'name' : u'''XENOPHILES''',
        'description': u'''The natives of this world are fast friends with a particular alien race. The aliens may have saved the planet at some point in the past, or awed the locals with superior tech or impressive cultural qualities. The aliens might even be the ruling class on the planet.''',
        'enemies': u'''Offworld xenophobe, Suspicious alien leader, Xenocultural imperialist''',
        'friends': u'''Benevolent alien, Native malcontent, Gone-native offworlder''',
        'complications': u'''The enthusiasm is due to alien psionics or tech, The enthusiasm is based on a lie, The aliens strongly dislike their \"groupies\", The aliens feel obliged to rule humanity for its own good, Humans badly misunderstand the aliens''',
        'things': u'''Hybrid alien-human tech, Exotic alien crafts, Sophisticated xenolinguistic and xenocultural research data''',
        'places': u'''Alien district, Alien-influenced human home, Cultural festival celebrating alien artist''',
      },
      
      'XENOPHOBES' : {
        'name' : u'''XENOPHOBES''',
        'description': u'''The natives are intensely averse to dealings with outworlders. Whether through cultural revulsion, fear of tech contamination, or a genuine immunodeficiency, the locals shun foreigners from offworld and refuse to have anything to do with them beyond the bare necessities of contact. Trade may or may not exist on this world, but if it does, it is almost certainly conducted by a caste of untouchables and outcasts.''',
        'enemies': u'''Revulsed local ruler, Native convinced some wrong was done to him, Cynical demagogue''',
        'friends': u'''Curious native, Exiled former ruler, Local desperately seeking outworlder help''',
        'complications': u'''The natives are symptomless carriers of a contagious and dangerous disease, The natives are exceptionally vulnerable to offworld diseases, The natives require elaborate purification rituals after speaking to an offworlder or touching them, The local ruler has forbidden any mercantile dealings with outworlders''',
        'things': u'''Jealously-guarded precious relic, Local product under export ban, Esoteric local technology''',
        'places': u'''Sealed treaty port, Public ritual not open to outsiders, Outcaste slum home''',
      },
      
      'ZOMBIES' : {
        'name' : u'''ZOMBIES''',
        'description': u'''This menace may not take the form of shambling corpses, but some disease, alien artifact, or crazed local practice produces men and women with habits similar to those of murderous cannibal undead. These outbreaks may be regular elements in local society, either provoked by some malevolent creators or the consequence of some local condition.''',
        'enemies': u'''Soulless maltech biotechnology cult, Sinister governmental agent, Crazed zombie cultist''',
        'friends': u'''Survivor of an outbreak, Doctor searching for a cure, Rebel against the secret malefactors''',
        'complications': u'''The zombies retain human intelligence, The zombies can be cured, The process is voluntary among devotees, The condition is infectious''',
        'things': u'''Cure for the condition, Alien artifact that causes it, Details of the cult\'s conversion process''',
        'places': u'''House with boarded-up windows, Dead city, Fortified bunker that was overrun from within''',
      }
      
    }


def get_tags(n=2):
    a = table_tags.keys()
    random.shuffle(a)
    res = []
    for h in range(0,n):
        res.append(table_tags[a[h]])
    return res

class StarSystem:
    def __init__(self,Name = Places.get_place(),x=0,y=0):
        self.initialize_data(Name)
        self.coords= (x,y)
        self.hidden = False
        self.linked_to = None

    def initialize_data(self,Name = None):
        self.initialize_simple_data(Name)
        self.tags =  get_tags()

    def initialize_simple_data(self,Name = None):
        if (Name != None):
            self.name = Name
        self.atmosphere =  get_table1("Atmosphere", table_atmosphere)
        self.biosphere =  get_table1("Biosphere", table_biosphere)
        self.temperature =  get_table1("Temperature", table_temperature)
        self.tech =  get_table1("Tech", table_tech)
        #print table_population
        self.population = get_table2("Population", table_population) 
        
    def link_to(self,other_system):
        self.linked_to = other_system
        other_system.linked_to = self

    def str_html(self):
        res = """
        <div class='world'>
        <h2>%s</h2>
        <div class='info_world'>
            <table class='tab_world'><tr>
                <th>Atmosphere</th><td>%s</td>
                </tr><tr><th>Biosphere</th><td>%s</td>
                </tr><tr><th>Temperature</th><td>%s</td>
                </tr><tr><th>Tech</th><td>%s</td>
                </tr><tr><th>Population</th><td>%s (%s)</td>
            </tr>
            </table>
        </div>
        <div class='tags'>
            <div class='tag_1'>%s</div>
            <div class='tag_2'>%s</div>
        </div>
        </div>
        """ % (self.name, self.atmosphere["Description"], self.biosphere["Description"], 
               self.temperature["Description"], self.tech["Description"], self.population["Description"],
               "{:,}".format(self.population["Population"]),self.__tag_html(0), self.__tag_html(1))
        return res

    def __tag_html(self,h = 0):
        tag = self.tags[h]
        tag_res = """    
    <h3>%s</h3>
    <dl>
        <dt>Description</dt>
        <dd>%s</dd>
        <dt>Enemies</dt>
        <dd>%s</dd>
        <dt>Friends</dt>
        <dd>%s</dd>
        <dt>Complications</dt>
        <dd>%s</dd>
        <dt>Things</dt>
        <dd>%s</dd>
        <dt>Places</dt>
        <dd>%s</dd>
    </dl>
        """ % (tag['name'],
              tag['description'], 
              tag ['enemies'],
              tag['friends'],
              tag['complications'],
              tag['things'],
              tag['places']) 
        return tag_res   
    
    
    def __tag_str(self,n=0):
        tag = self.tags[n]
        tag_res = """
%s
    * Description: %s
    * Enemies: %s
    * Friends: %s
    * Complications: %s
    * Things: %s
    * Places: %s
        """ % (tag['name'],
              tag['description'], 
              tag ['enemies'],
              tag['friends'],
              tag['complications'],
              tag['things'],
              tag['places']) 
        return tag_res   
    
    def __str__(self):
        res = """
-----------------------------------------------
%s
-----------------------------------------------
Atmosphere: %s
Biosphere: %s
Temperature: %s
Tech: %s
Population: %s (%s)

-----------------------------------------------
Tags:
-----------------------------------------------

%s

%s
        
        """ % (self.name,
               self.atmosphere["Description"],
               self.biosphere["Description"],
               self.temperature["Description"],
               self.tech["Description"],
               self.population["Description"],
               self.population["Population"],
               self.__tag_str(), self.__tag_str(1))
        return res

class Sector:
    def __init__(self,m_name = Places.get_place()):
        self.name = m_name
        num_sys =  Dice.d10(1, 20)
        self.systems = {}
        self.links = {}
        for h in range(0,num_sys):
            coord = (Dice.dN(8, 1, 0),Dice.d10())
            while coord in self.systems.keys():
                coord = (Dice.dN(8, 1, 0),Dice.d10())
            w = Dice.d6()
            system = StarSystem(get_place(), coord[0], coord[1])
            #print "w is",w
            if w == 3:
                system.hidden = True
            else:
                system.hidden = False
            self.systems[coord] = system

    def add_new_system (self,coord):
        system = StarSystem(get_place(), coord[0], coord[1])
        self.systems[coord] = system
        return system
        
    def remove_system (self,coord):
        del self.systems[coord]

    def __str__(self):
        s = "Sector: %s\n\n" % self.name
        for k in self.systems.keys():
            s += str(self.systems[k])
        return s
       
    def str_html(self): 
        html = ""
        for k in self.systems.keys():
            html += self.systems[k].str_html()

        res = """
        <h1>%s Sector</h1>
        %s
        """ % (self.name, html)
        return res

    def save_sector(self,filename):
        shelf = shelve.open(filename)
        shelf["SWNSector"] = self
        
def deserialize_sector(filename):
    shelf = shelve.open(filename)
    return shelf["SWNSector"]

if __name__ == '__main__':        
    pass
    #s = Sector()
    #print s.str_html()

#for k in s.keys():
#    print k, s[k]