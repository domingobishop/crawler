# https://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
# import libraries
import nltk

data = [
    ('The UKs spending watchdog has called the project risky and expensive.', 'negative'),
    ('The Initiative on Global Markets panel of economic experts was recently asked about the Republican tax plan.', 'neutral'),
    ('GWR unveiled its new trains in October, with up to two hanging bike storage spaces per carriage.', 'positive'),
    ('In the days of London smogs it was possible to both see pollution and smell it.', 'negative'),
    ('There was a sense of disbelief that I had been so close, a clumsy intruder among this wild tangle of trees.', 'negative'),
    ('And one by one, each of the big four Australian banks ruled out financing the mine.', 'positive'),
    ('Fusion power is one of the most sought-after technological goals in the pursuit of clean energy.', 'positive'),
    ('It is arguing that the switch to electric transport will drive up future demand.', 'positive'),
    ('Winter riding in rural areas can be more tricky, but even modern lights can make it much easier.', 'positive'),
    ('Chung said traffic pollution might also affect younger people doing their shopping in the heart of a city.', 'negative'),
    ('Food sustainability map Crossley said this highlighted the challenge facing the UK as Brexit approached.', 'negative'),
    ('North Alaska is the countrys last frontier, and hes letting the oil industry suck the life out of it.', 'negative'),
    ('What the report also shows is that the biggest uncertainty in future climate change is us.', 'negative'),
    ('The 2015 Paris Accord recognised the contribution of indigenous knowledge in dealing with climate change.', 'positive'),
    ('No society can afford to ignore air pollution.', 'negative'),
    ('In the Facebook ad the car was described as a clean car and helps to give back to the environment.', 'positive'),
    ('Ask How could the UK deal with plastic waste without exporting it?', 'neutral'),
    ('Alberto Bai, a Matsés traditional healer, in the healing forest near Buenas Lomas Nueva in Perus Amazon.', 'neutral'),
    ('Liberating the earth means defending the land, says José Rene Guetio, a Nasa elder.', 'positive'),
    ('Will Norman is Londons walking and cycling commissioner', 'neutral'),
    ('Because polar bears rely on sea ice to hunt seals, global warming also threatens their species.', 'negative'),
    ('The US Global Change Research Program recently released a Climate Science Special Report.', 'neutral'),
    ('The first main chapter deals with changes to the climate and focuses much attention on global temperatures.', 'neutral'),
    ('No society can afford to ignore air pollution.', 'negative'),
    ('The Luxembourg-based court of justice of the European Union is the highest court in Europe.', 'neutral'),
    ('Brexit makes the headlines every day without fail, even when nothing has happened.', 'negative'),
    ('They should not allow the popularity of the term populism to mask the nativism of the radical right.', 'negative'),
    ('In November, Momentum said it had spent £38,743 on the general election campaign.', 'neutral'),
    ('Quiet meetings on Brexit took place between civil servants in Ireland and Northern Ireland.', 'neutral'),
    ('By 2016, David Camerons austerity agenda had seen child poverty rates shoot up to 30%.', 'negative'),
    ('The DUP leader also sought to repair some of the damaged relations with the Irish government on Wednesday.', 'neutral'),
    ('There is a risk that a Tories versus the police row will have a domino effect on her cabinet.', 'negative'),
    ('Britains exit from the EU  taking Northern Ireland with it  risks a return to a hard or policed border.', 'negative'),
    ('Yet rather than stay shoulder to shoulder with the Union, the British chose to be on their own again.', 'negative'),
    ('‘The Tories economic strategy failed on its own stated terms.', 'negative'),
    ('Adonis criticised Johnson on Twitter for failing to speak out against high pay packets.', 'negative'),
    ('Others have urged the government to ensure that EU funding is replaced from 2019 onwards.', 'neutral'),
    ('The Health and Safety Executives myth-busting website has to rebut such nonsense every week.', 'negative'),
    ('My experience of employing disabled people is that they are brilliant employees.', 'positive'),
    ('The new defence secretary told the Daily Mail: A dead terrorist cant cause any harm to Britain.', 'negative'),
    ('A meeting to discuss them was scheduled for 31 May, but the attack at Manchester Arena happened on 22 May.', 'negative'),
    ('A number of big, unanswered questons about ACOs remain, despite their imminent arrival in the NHS, he adds.', 'neutral'),
    ('London depends on foreign workers to keep growing and therefore keep boosting that tax export.', 'positive'),
    ('There were signs that progress was being made towards a deal to avoid a hard border on the island of Ireland.', 'positive'),
    ('I will also discuss with House officials the steps necessary to repay previous travel claims.', 'positive'),
    ('When those disasters happen, media outlets need to cover them as climate change stories.', 'neutral'),
    ('Just 25% of Americans support the tax plan, though that includes 60% of Republican voters.', 'negative'),
    ('Because polar bears rely on sea ice to hunt seals, global warming also threatens their species.', 'negative'),
    ('The UK, where coal use will end by 2025, has gone from 40% of coal-fired electricity to 2% since 2012.', 'positive'),
    ('Saving the vaquita now rests with the Mexican government, which might somehow be able to end the illegal fishing for the totoaba.', 'positive'),
    ('If no further action is taken, GLA figures show that by 2041, three days would be lost per person every year due to congestion.', 'negative'),
    ('Timber planks at an illegal logging site discovered by the Palawan NGO Network Inc (PNNI) near the tourist town of El Nido.', 'negative'),
    ('The Kokonuko blame the police, who they say wanted to silence the community and scare them away from the land.', 'negative'),
    ('It seems that indigenous crops are gaining recognition in the African farming context.', 'positive'),
    ('Today is the turn of the environmental health officers (EHOs) to peer into the fog of possible Brexit futures at their annual conference.', 'neutral'),
    ('The government also defended Britains need for new nuclear power in the face of falling renewable costs.', 'negative'),
    ('In 2016, China imported 7.3m tonnes of waste plastics from developed countries including the UK, the US and Japan.', 'negative'),
    ('Using the Wingtags app for Android and iOS, turkey fans can report sightings of tagged birds, to help us find out whos going where.', 'positive'),
    ('Back in the National Forest, Everitt says they are doing their bit to promote tree planting.', 'positive'),
    ('There are other (better) ways to measure climate change such as heat absorbed by the oceans, melting ice, sea level rise, or others.', 'positive'),
    ('The 2015 Paris Accord recognised the contribution of indigenous knowledge in dealing with climate change.', 'positive'),
    ('National monuments are protected sites of historical, cultural or scientific interest managed by a patchwork of federal agencies.', 'neutral'),
    ('In the winter, riding sedately in office clothes can feel much easier than juggling two sets of winter garments.', 'positive'),
    ('The forces armed response vehicles usually carry two officers.', 'neutral'),
    ('No, Im not going to the office Christmas party this year, and yes, Im feeling pretty happy about it.', 'positive'),
    ('EU citizens in the UK and UK citizens in the rest of the EU have the right to stay.', 'positive'),
    ('The fire north of San Diego began next to state highway 76 with strong winds carrying it across six lanes to the other side.', 'negative'),
    ('The security bug is just the latest in a series of issues affecting Apples software on both its iPhone and Mac computers.', 'negative'),
    ('Eighteen months of bluster, of Brexit means Brexit, of red, white and blue Brexit, of No deal is better than a bad deal.', 'negative'),
    ('Investigators say that Camorra bosses forced bars to buy a coffee brand owned by the feared DAlterio family.', 'negative'),
    ('Two-thirds of teenagers told a recent survey for Digital Awareness UK that they wouldnt care if social media had never been invented.', 'neutral'),
    ('Progress may depend on his conversations in two days of talks with senior Iranian figures including the foreign minister, Javad Zarif.', 'neutral'),
    ('I increasingly felt less welcome: Martin Seeleib-Kaiser, 53, German Returned in 2017', 'negative'),
    ('He admitted finding it weird he again was not in the top three last year despite winning double gold at the 2016 Rio Olympics.', 'negative'),
    ('Too many men were locked up for significant periods of the day, often as long as 23 hours, the report said.', 'negative'),
    ('But it is clear that HMRC did not levy the biggest fine possible on Sports Direct  which would amount to double the wages owed, nearly £2m.', 'negative'),
    ('Five firefighters spent an hour working to release a YouTube prankster who had cemented his head inside a microwave oven.', 'positive'),
    ('The number of hate crimes against LGBT people in Russia has doubled in five years, according to new research.', 'negative'),
    ('We know that North Korea wants above all to talk to the United States about guarantees for its security.', 'neutral'),
    ('I had recently started primary school when I was told my mother was going to die.', 'negative'),
    ('Ive got no home to go back to … tomorrow I wont have anywhere to sleep, says Lis neighbour, a migrant from Anhui who asked not to be named.', 'negative'),
    ('On Thursday, McKenzie posted to Facebook that there were no blurry lines during that awkward days filming in 1991.', 'neutral'),
    ('But arthouse and horror have more in common than aficionados of either type of film would care to admit.', 'neutral'),
    ('Pope Francis has called for the wording of the Lords Prayer to be changed, because it implies God induces temptation.', 'neutral'),
    ('The water from the river normally generates a total of 300 megawatts of electricity, which is 98% of the countrys supply.', 'positive'),
    ('As the Paradise and Panama Papers have shown, the super-rich and powerful cant be trusted to regulate themselves, Corbyn will say.', 'negative'),
    ('We need better ways of assessing the emotional and mental health needs of children going into care.', 'neutral'),
    ('Hart was badly failed by every NHS service that was meant to be caring for her from August 2012, Kirkup found.', 'negative'),
    ('The last two years  it was an extraordinary time for me and the service to Poland and Poles was an honour, Szydło said on Twitter.', 'positive')
]


def create_training_data():
    tweets = []
    for (words, sentiment) in data:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 4]
        tweets.append((words_filtered, sentiment))
    return tweets


training_data = [
    (['spending', 'watchdog', 'project', 'risky', 'expensive'], 'negative'),
    (['initiative', 'global', 'markets', 'panel', 'economic', 'experts', 'republican', 'plan'], 'neutral'),
    (['unveiled', 'trains', 'october,', 'hanging', 'bike', 'storage', 'spaces', 'carriage'], 'positive'),
    (['london', 'smogs', 'possible', 'pollution', 'smell'], 'negative'),
    (['sense', 'disbelief', 'close,', 'clumsy', 'intruder', 'wild', 'tangle', 'trees'], 'negative'),
    (['australian', 'banks', 'ruled', 'financing', 'mine'], 'positive'),
    (['fusion', 'power', 'technological', 'goals', 'pursuit', 'clean', 'energy'], 'positive'),
    (['arguing', 'switch', 'electric', 'transport', 'drive', 'future', 'demand'], 'positive'),
    (['winter', 'riding', 'rural', 'modern', 'lights', 'make', 'much', 'easier'], 'positive'),
    (['chung', 'traffic', 'pollution', 'younger', 'people', 'shopping', 'heart', 'city'], 'negative'),
    (['food', 'sustainability', 'highlighted', 'challenge', 'facing', 'brexit', 'approached'], 'negative'),
    (['north', 'alaska', 'industry', 'suck', 'life'], 'negative'),
    (['report', 'biggest', 'uncertainty', 'future', 'climate', 'change'], 'negative'),
    (['2015', 'paris', 'recognised', 'contribution', 'indigenous', 'knowledge', 'climate', 'change'], 'positive'),
    (['society', 'afford', 'ignore', 'pollution'], 'negative'),
    (['facebook', 'clean', 'helps', 'environment'], 'positive'),
    (['deal', 'plastic', 'waste', 'without', 'exporting'], 'neutral'),
    (['alberto', 'traditional', 'healer,', 'healing', 'forest', 'amazon'], 'neutral'),
    (['liberating', 'earth', 'defending', 'land,', 'josé', 'rene', 'guetio,', 'nasa', 'elder'], 'positive'),
    (['norman', 'londons', 'walking', 'cycling', 'commissioner'], 'neutral'),
    (['polar', 'bears', 'hunt', 'seals,', 'global', 'warming', 'threatens', 'species'], 'negative'),
    (['global', 'change', 'research', 'program', 'climate', 'science', 'special', 'report'], 'neutral'),
    (['deals', 'changes', 'climate', 'focuses', 'global', 'temperatures'], 'neutral'),
    (['society', 'afford', 'ignore', 'pollution'], 'negative'),
    (['luxembourg-based', 'court', 'justice', 'european', 'union', 'highest', 'court', 'europe'], 'neutral'),
    (['brexit', 'makes', 'headlines', 'fail,'], 'negative'),
    (['popularity', 'term', 'populism', 'nativism', 'radical', 'right'], 'negative'),
    (['november,', 'momentum', 'spent', 'general', 'election', 'campaign'], 'neutral'),
    (['quiet', 'meetings', 'brexit', 'civil', 'servants', 'ireland', 'northern', 'ireland'], 'neutral'),
    (['2016,', 'david', 'camerons', 'austerity', 'agenda', 'child', 'poverty', 'rates'], 'negative'),
    (['leader', 'damaged', 'relations', 'irish', 'government'], 'neutral'),
    (['risk', 'tories', 'versus', 'police', 'domino', 'effect', 'cabinet'], 'negative'),
    (['britains', 'exit', 'northern', 'ireland', 'risks', 'hard', 'policed', 'border'], 'negative'),
    (['rather', 'stay', 'union,', 'british'], 'negative'),
    (['tories', 'economic', 'strategy', 'failed', 'stated', 'terms'], 'negative'),
    (['adonis', 'criticised', 'johnson', 'twitter', 'failing', 'speak', 'against', 'high', 'packets'], 'negative'),
    (['urged', 'government', 'ensure', 'funding', 'replaced', 'onwards'], 'neutral'),
    (['health', 'safety', 'executives', 'myth-busting', 'website', 'rebut', 'nonsense'], 'negative'),
    (['experience', 'employing', 'disabled', 'people', 'brilliant', 'employees'], 'positive'),
    (['defence', 'secretary', 'daily', 'mail', 'dead', 'terrorist', 'harm', 'britain'], 'negative'),
    (['meeting', 'discuss', 'scheduled', 'may,', 'attack', 'manchester', 'arena', 'may'], 'negative'),
    (['unanswered', 'questons', 'acos', 'remain,', 'despite', 'imminent', 'arrival', 'nhs,'], 'neutral'),
    (['london', 'foreign', 'workers', 'keep', 'growing', 'boosting', 'export'], 'positive'),
    (['progress', 'deal', 'avoid', 'hard', 'border', 'island', 'ireland'], 'positive'),
    (['discuss', 'house', 'officials', 'necessary', 'repay', 'previous', 'travel', 'claims'], 'positive'),
    (['disasters', 'media', 'outlets', 'climate', 'change', 'stories'], 'neutral'),
    (['americans', 'support', 'plan,', 'republican', 'voters'], 'negative'),
    (['polar', 'bears', 'rely', 'hunt', 'seals', 'global', 'warming', 'threatens', 'species'], 'negative'),
    (['coal', '2025,', 'coal-fired', 'electricity', 'since', '2012'], 'positive'),
    (['saving', 'vaquita', 'mexican', 'government,', 'illegal', 'fishing', 'totoaba'], 'positive'),
    (['action', 'figures', 'show', '2041,', 'lost', 'person', 'congestion'], 'negative'),
    (['timber', 'planks', 'illegal', 'logging', 'site', 'discovered', 'palawan', 'network', 'tourist', 'town', 'nido'], 'negative'),
    (['kokonuko', 'blame', 'police,', 'wanted', 'silence', 'community', 'scare', 'away', 'land'], 'negative'),
    (['indigenous', 'crops', 'gaining', 'recognition', 'african', 'farming', 'context'], 'positive'),
    (['environmental', 'health', 'officers', 'peer', 'brexit', 'futures', 'annual', 'conference'], 'neutral'),
    (['government', 'defended', 'britains', 'nuclear', 'power', 'face', 'falling', 'renewable', 'costs'], 'negative'),
    (['2016,', 'china', 'imported', 'waste', 'plastics', 'developed', 'countries', 'japan'], 'negative'),
    (['using', 'wingtags', 'android', 'ios,', 'turkey', 'fans', 'report', 'sightings', 'tagged', 'birds,', 'help'], 'positive'),
    (['national', 'forest,', 'everitt', 'promote', 'tree', 'planting'], 'positive'),
    (['measure', 'climate', 'change', 'heat', 'absorbed', 'oceans,', 'melting', 'ice,', 'level', 'rise'], 'positive'),
    (['2015', 'paris', 'accord', 'recognised', 'contribution', 'indigenous', 'knowledge', 'dealing', 'climate', 'change'], 'positive'),
    (['national', 'monuments', 'protected', 'sites', 'historical,', 'cultural', 'scientific', 'interest', 'managed', 'patchwork', 'federal', 'agencies'], 'neutral'),
    (['winter,', 'riding', 'sedately', 'office', 'clothes', 'easier', 'juggling', 'winter', 'garments'], 'positive'),
    (['forces', 'armed', 'response', 'vehicles', 'usually', 'carry', 'officers'], 'neutral'),
    (['office', 'christmas', 'party', 'year,', 'feeling', 'pretty', 'happy'], 'positive'),
    (['eu', 'citizens', 'right', 'stay'], 'positive'),
    (['fire', 'north', 'diego', 'highway', 'strong', 'winds'], 'negative'),
    (['security', 'issues', 'affecting', 'apples', 'software', 'iphone', 'computers'], 'negative'),
    (['eighteen', 'bluster,', 'brexit', 'red,', 'white', 'blue', 'deal', 'better', 'deal'], 'negative'),
    (['investigators', 'camorra', 'bosses', 'forced', 'bars', 'coffee', 'brand', 'owned', 'feared', 'dalterio', 'family'], 'negative'),
    (['two-thirds', 'teenagers', 'survey', 'digital', 'awareness', 'care', 'social', 'media', 'never', 'invented'], 'neutral'),
    (['progress', 'depend', 'conversations', 'days', 'talks', 'senior', 'iranian', 'figures', 'including', 'foreign', 'minister', 'javad', 'zarif'], 'neutral'),
    (['increasingly', 'felt', 'less', 'welcome', 'martin', 'seeleib-kaiser,', 'german', 'returned', '2017'], 'negative'),
    (['admitted', 'finding', 'weird', 'again', 'three', 'last', 'year', 'despite', 'winning', 'double', 'gold', '2016', 'olympics'], 'negative'),
    (['locked', 'significant', 'periods', 'day', 'often', 'long', 'hours,', 'report'], 'negative'),
    (['hmrc', 'levy', 'biggest', 'fine', 'sports', 'direct', 'amount', 'double', 'wages', 'owed'], 'negative'),
    (['firefighters', 'spent', 'hour', 'youtube', 'prankster', 'cemented', 'head', 'microwave', 'oven'], 'positive'),
    (['hate', 'crimes', 'against', 'lgbt', 'people', 'russia', 'doubled', 'five', 'years,', 'according', 'research'], 'negative'),
    (['north', 'korea', 'wants', 'talk', 'united', 'states', 'guarantees', 'security'], 'neutral'),
    (['recently', 'started', 'primary', 'school', 'mother', 'going', 'die'], 'negative'),
    (['home', 'tomorrow', 'sleep,', 'neighbour,', 'migrant', 'anhui', 'named'], 'negative'),
    (['mckenzie', 'posted', 'facebook', 'blurry', 'lines', 'during', 'awkward', 'days', 'filming', '1991'], 'neutral'),
    (['arthouse', 'horror', 'common', 'aficionados', 'either', 'type', 'film', 'would', 'care', 'admit'], 'neutral'),
    (['pope', 'francis', 'wording', 'lords', 'prayer', 'changed,', 'implies', 'induces', 'temptation'], 'neutral'),
    (['water', 'river', 'normally', 'generates', 'total', 'megawatts', 'electricity,', 'supply'], 'positive'),
    (['paradise', 'panama', 'papers', 'super-rich', 'powerful', 'trusted', 'regulate', 'themselves', 'corbyn'], 'negative'),
    (['better', 'assessing', 'emotional', 'mental', 'health', 'needs', 'children', 'care'], 'neutral'),
    (['hart', 'badly', 'failed', 'service', 'meant', 'caring', 'august', '2012,', 'kirkup', 'found'], 'negative'),
    (['last', 'years', 'extraordinary', 'time', 'service', 'poland', 'poles', 'honour,', 'szydło', 'twitter'], 'positive')
]

test_data = [
    (['defendant', 'leadership', 'role', 'within', 'federal', 'officials', 'said'], 'neutral'),
    (['uks', 'spending', 'watchdog', 'called', 'project', 'risky', 'expensive'], 'negative'),
    (['initiative', 'global', 'markets', 'panel', 'economic', 'experts', 'was', 'recently', 'republican', 'tax', 'plan'], 'neutral'),
    (['gwr', 'unveiled', 'its', 'new', 'trains', 'october,', 'two', 'hanging', 'bike', 'storage', 'spaces', 'per', 'carriage'], 'positive'),
    (['days', 'london', 'smogs', 'was', 'possible', 'see', 'pollution', 'smell'], 'negative'),
    (['was', 'sense', 'disbelief', 'close,', 'clumsy', 'intruder', 'among', 'wild', 'tangle', 'trees'], 'negative')
]


def get_words_in_tweets(data):
    all_words = []
    for (words, sentiment) in data:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


word_features = get_word_features(get_words_in_tweets(training_data))

training_set = nltk.classify.apply_features(extract_features, training_data)

classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'There is recognition'
print(classifier.classify(extract_features(tweet.split())))
