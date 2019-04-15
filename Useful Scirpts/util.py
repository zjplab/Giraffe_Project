
default_categories=['aardvark',
  'aardwolf',
  'baboon',
  'batEaredFox',
  'buffalo',
  'bushbuck',
  'caracal',
  'cheetah',
  'civet',
  'dikDik',
  'eland',
  'elephant',
  'empty',
  'gazelleGrants',
  'gazelleThomsons',
  'genet',
  'giraffe',
  'guineaFowl',
  'hare',
  'hartebeest',
  'hippopotamus',
  'honeyBadger',
  'hyenaSpotted',
  'hyenaStriped',
  'impala',
  'jackal',
  'koriBustard',
  'leopard',
  'lionFemale',
  'lionMale',
  'mongoose',
  'ostrich',
  'otherBird',
  'porcupine',
  'reedbuck',
  'reptiles',
  'rhinoceros',
  'rodents',
  'secretaryBird',
  'serval',
  'topi',
  'vervetMonkey',
  'warthog',
  'waterbuck',
  'wildcat',
  'wildebeest',
  'zebra',
  'zorilla']

def score_output(scores: list, categories:list=default_categories):
    ''' useful code: 
    torch.item(): convert a single torch element to python corresponding 
    type
    torch.tolist(): similaryly, to a python list
    
    output percentages of confidence score for each category 
    '''
    sort_scores=list(zip(categories, scores))
    sort_scores=sorted(sort_scores, key=lambda x:x[1], reverse=True)
    total=sum( (score for _, score in sort_scores) )
    sort_scores=[ (cat, score/total) for cat, score in sort_scores]
    return sort_scores

