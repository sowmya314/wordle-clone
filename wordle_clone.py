# Wordle
# A variation on the New York Times Wordle Game
# Sowmya Ramanan

from time import sleep
import os
import random

WORDS = ['which', 'there', 'their', 'about', 'would', 'these', 'other', 'words', 'could', 'write', 'first', 'water', 'after', 'where', 'right', 'think', 'three', 'years', 'place', 'sound', 'great', 'again', 'still', 'every', 'small', 'found', 'those', 'never', 'under', 'might', 'while', 'house', 'world', 'below', 'asked', 'going', 'large', 'until', 'along', 'shall', 'being', 'often', 'earth', 'began', 'since', 'study', 'night', 'light', 'above', 'paper', 'parts', 'young', 'story', 'point', 'times', 'heard', 'whole', 'white', 'given', 'means', 'music', 'miles', 'thing', 'today', 'later', 'using', 'money', 'lines', 'order', 'group', 'among', 'learn', 'known', 'space', 'table', 'early', 'trees', 'short', 'hands', 'state', 'black', 'shown', 'stood', 'front', 'voice', 'kinds', 'makes', 'comes', 'close', 'power', 'lived', 'vowel', 'taken', 'built', 'heart', 'ready', 'quite', 'class', 'bring', 'round', 'horse', 'shows', 'piece', 'green', 'stand', 'birds', 'start', 'river', 'tried', 'least', 'field', 'whose', 'girls', 'leave', 'added', 'color', 'third', 'hours', 'moved', 'plant', 'doing', 'names', 'forms', 'heavy', 'ideas', 'cried', 'check', 'floor', 'begin', 'woman', 'alone', 'plane', 'spell', 'watch', 'carry', 'wrote', 'clear', 'named', 'books', 'child', 'glass', 'human', 'takes', 'party', 'build', 'seems', 'blood', 'sides', 'seven', 'pasta', 'mouth', 'solve', 'north', 'value', 'death', 'maybe', 'happy', 'tells', 'gives', 'looks', 'shape', 'lives', 'steps', 'areas', 'sense', 'speak', 'force', 'ocean', 'speed', 'women', 'metal', 'south', 'grass', 'scale', 'cells', 'lower', 'sleep', 'wrong', 'pages', 'ships', 'needs', 'rocks', 'eight', 'major', 'level', 'total', 'ahead', 'reach', 'stars', 'store', 'sight', 'terms', 'catch', 'works', 'board', 'cover', 'songs', 'equal', 'stone', 'waves', 'guess', 'dance', 'spoke', 'break', 'cause', 'radio', 'weeks', 'lands', 'basic', 'liked', 'trade', 'fresh', 'final', 'fight', 'meant', 'drive', 'spent', 'local', 'waxes', 'knows', 'train', 'bread', 'homes', 'teeth', 'coast', 'thick', 'brown', 'clean', 'quiet', 'sugar', 'facts', 'steel', 'forth', 'rules', 'notes', 'units', 'peace', 'month', 'verbs', 'seeds', 'helps', 'sharp', 'visit', 'woods', 'chief', 'walls', 'cross', 'wings', 'grown', 'cases', 'foods', 'crops', 'fruit', 'stick', 'wants', 'stage', 'sheep', 'nouns', 'plain', 'drink', 'bones', 'apart', 'turns', 'moves', 'touch', 'angle', 'based', 'range', 'marks', 'tired', 'older', 'farms', 'spend', 'shoes', 'goods', 'chair', 'acorn', 'twice', 'cents', 'empty', 'alike', 'style', 'broke', 'pairs', 'count', 'enjoy', 'score', 'shore', 'roots', 'paint', 'heads', 'shook', 'serve', 'angry', 'crowd', 'wheel', 'quick', 'dress', 'share', 'alive', 'noise', 'solid', 'cloth', 'signs', 'hills', 'types', 'drawn', 'worth', 'truck', 'piano', 'upper', 'loved', 'usual', 'faces', 'drove', 'cabin', 'boats', 'towns', 'proud', 'court', 'model', 'prime', 'fifty', 'plans', 'yards', 'prove', 'tools', 'price', 'sheet', 'smell', 'boxes', 'raise', 'match', 'truth', 'roads', 'threw', 'enemy', 'lunch', 'chart', 'scene', 'graph', 'doubt', 'guide', 'winds', 'block', 'grain', 'smoke', 'mixed', 'games', 'wagon', 'sweet', 'topic', 'extra', 'plate', 'title', 'knife', 'fence', 'falls', 'cloud', 'wheat', 'plays', 'enter', 'broad', 'steam', 'atoms', 'press', 'lying', 'basis', 'clock', 'taste', 'grows', 'thank', 'storm', 'agree', 'brain', 'track', 'smile', 'funny', 'beach', 'stock', 'hurry', 'saved', 'sorry', 'giant', 'trail', 'offer', 'ought', 'rough', 'daily', 'avoid', 'keeps', 'throw', 'allow', 'cream', 'laugh', 'edges', 'teach', 'frame', 'bells', 'dream', 'magic', 'occur', 'ended', 'chord', 'false', 'skill', 'holes', 'dozen', 'brave', 'apple', 'climb', 'outer', 'pitch', 'ruler', 'holds', 'fixed', 'costs', 'calls', 'blank', 'staff', 'labor', 'eaten', 'youth', 'tones', 'honor', 'globe', 'gases', 'doors', 'poles', 'loose', 'apply', 'tears', 'exact', 'brush', 'chest', 'layer', 'whale', 'minor', 'faith', 'tests', 'judge', 'items', 'worry', 'waste', 'hoped', 'strip', 'begun', 'aside', 'lakes', 'bound', 'depth', 'candy', 'event', 'worse', 'aware', 'shell', 'rooms', 'ranch', 'image', 'snake', 'aloud', 'dried', 'likes', 'motor', 'pound', 'knees', 'refer', 'fully', 'chain', 'shirt', 'flour', 'drops', 'spite', 'orbit', 'banks', 'shoot', 'curve', 'tribe', 'tight', 'blind', 'slept', 'shade', 'claim', 'flies', 'theme', 'queen', 'fifth', 'union', 'hence', 'straw', 'entry', 'issue', 'birth', 'feels', 'anger', 'brief', 'rhyme', 'glory', 'guard', 'flows', 'flesh', 'owned', 'trick', 'yours', 'sizes', 'noted', 'width', 'burst', 'route', 'lungs', 'uncle', 'bears', 'royal', 'kings', 'forty', 'trial', 'cards', 'brass', 'opera', 'chose', 'owner', 'vapor', 'beats', 'mouse', 'tough', 'wires', 'meter', 'tower', 'finds', 'inner', 'stuck', 'arrow', 'poems', 'label', 'swing', 'solar', 'truly', 'tense', 'beans', 'split', 'rises', 'weigh', 'hotel', 'stems', 'pride', 'swung', 'grade', 'digit', 'badly', 'boots', 'pilot', 'sales', 'swept', 'lucky', 'prize', 'stove', 'tubes', 'acres', 'wound', 'steep', 'slide', 'trunk', 'error', 'porch', 'slave', 'exist', 'faced', 'mines', 'marry', 'juice', 'raced', 'waved', 'goose', 'trust', 'fewer', 'favor', 'mills', 'views', 'joint', 'eager', 'spots', 'blend', 'rings', 'adult', 'index', 'nails', 'horns', 'balls', 'flame', 'rates', 'drill', 'trace', 'skins', 'waxed', 'seats', 'stuff', 'ratio', 'minds', 'dirty', 'silly', 'coins', 'hello', 'trips', 'leads', 'rifle', 'hopes', 'bases', 'shine', 'bench', 'moral', 'fires', 'meals', 'shake', 'shops', 'cycle', 'movie', 'slope', 'canoe', 'teams', 'folks', 'fired', 'bands', 'thumb', 'shout', 'canal', 'habit', 'reply', 'ruled', 'fever', 'crust', 'shelf', 'walks', 'midst', 'crack', 'print', 'tales', 'coach', 'stiff', 'flood', 'verse', 'awake', 'rocky', 'march', 'fault', 'swift', 'faint', 'civil', 'ghost', 'feast', 'blade', 'limit', 'germs', 'reads', 'ducks', 'dairy', 'worst', 'gifts', 'lists', 'stops', 'rapid', 'brick', 'claws', 'beads', 'beast', 'skirt', 'cakes', 'lions', 'frogs', 'tries', 'nerve', 'grand', 'armed', 'treat', 'honey', 'moist', 'legal', 'penny', 'crown', 'shock', 'taxes', 'sixty', 'altar', 'pulls', 'sport', 'drums', 'talks', 'dying', 'dates', 'drank', 'blows', 'lever', 'wages', 'proof', 'drugs', 'tanks', 'sings', 'tails', 'pause', 'herds', 'arose', 'hated', 'clues', 'novel', 'shame', 'burnt', 'races', 'flash', 'weary', 'heels', 'token', 'coats', 'spare', 'shiny', 'alarm', 'dimes', 'sixth', 'clerk', 'mercy', 'sunny', 'guest', 'float', 'shone', 'pipes', 'worms', 'bills', 'sweat', 'suits', 'smart', 'upset', 'rains', 'sandy', 'rainy', 'parks', 'sadly', 'fancy', 'rider', 'unity', 'bunch', 'rolls', 'crash', 'craft', 'newly', 'gates', 'hatch', 'paths', 'funds', 'wider', 'grace', 'grave', 'tides', 'admit', 'shift', 'sails', 'pupil', 'tiger', 'angel', 'cruel', 'agent', 'drama', 'urged', 'patch', 'nests', 'vital', 'sword', 'blame', 'weeds', 'screw', 'vocal', 'bacon', 'chalk', 'cargo', 'crazy', 'acted', 'goats', 'arise', 'witch', 'loves', 'queer', 'dwell', 'backs', 'ropes', 'shots', 'merry', 'phone', 'cheek', 'peaks', 'ideal', 'beard', 'eagle', 'creek', 'cries', 'ashes', 'stall', 'yield', 'mayor', 'opens', 'input', 'fleet', 'tooth', 'cubic', 'wives', 'burns', 'poets', 'apron', 'spear', 'organ', 'cliff', 'stamp', 'paste', 'rural', 'baked', 'chase', 'slice', 'slant', 'knock', 'noisy', 'sorts', 'stays', 'wiped', 'blown', 'piled', 'clubs', 'cheer', 'widow', 'twist', 'tenth', 'hides', 'comma', 'sweep', 'spoon', 'stern', 'crept', 'maple', 'deeds', 'rides', 'muddy', 'crime', 'jelly', 'ridge', 'drift', 'dusty', 'devil', 'tempo', 'humor', 'sends', 'steal', 'tents', 'waist', 'roses', 'reign', 'noble', 'cheap', 'dense', 'linen', 'geese', 'woven', 'posts', 'hired', 'wrath', 'salad', 'bowed', 'tires', 'shark', 'belts', 'grasp', 'blast', 'polar', 'fungi', 'tends', 'pearl', 'loads', 'jokes', 'veins', 'frost', 'hears', 'loses', 'hosts', 'diver', 'phase', 'toads', 'alert', 'tasks', 'seams', 'coral', 'focus', 'naked', 'puppy', 'jumps', 'spoil', 'quart', 'macro', 'fears', 'flung', 'spark', 'vivid', 'brook', 'steer', 'spray', 'decay', 'ports', 'socks', 'urban', 'goals', 'grant', 'minus', 'films', 'tunes', 'shaft', 'firms', 'skies', 'bride', 'wreck', 'flock', 'stare', 'hobby', 'bonds', 'dared', 'faded', 'thief', 'crude', 'pants', 'flute', 'votes', 'tonal', 'radar', 'wells', 'skull', 'hairs', 'argue', 'wears', 'dolls', 'voted', 'caves', 'cared', 'broom', 'scent', 'panel', 'fairy', 'olive', 'bends', 'prism', 'lamps', 'cable', 'peach', 'ruins', 'rally', 'schwa', 'lambs', 'sells', 'cools', 'draft', 'charm', 'limbs', 'brake', 'gazed', 'cubes', 'delay', 'beams', 'fetch', 'ranks', 'array', 'harsh', 'camel', 'vines', 'picks', 'naval', 'purse', 'rigid', 'crawl', 'toast', 'soils', 'sauce', 'basin', 'ponds', 'twins', 'wrist', 'fluid', 'pools', 'brand', 'stalk', 'robot', 'reeds', 'hoofs', 'buses', 'sheer', 'grief', 'bloom', 'dwelt', 'melts', 'risen', 'flags', 'knelt', 'fiber', 'roofs', 'freed', 'armor', 'piles', 'aimed', 'algae', 'twigs', 'lemon', 'ditch', 'drunk', 'rests', 'chill', 'slain', 'panic', 'cords', 'tuned', 'crisp', 'ledge', 'dived', 'swamp', 'clung', 'stole', 'molds', 'yarns', 'liver', 'gauge', 'breed', 'stool', 'gulls', 'awoke', 'gross', 'diary', 'rails', 'belly', 'trend', 'flask', 'stake', 'fried', 'draws', 'actor', 'handy', 'bowls', 'haste', 'scope', 'deals', 'knots', 'moons', 'essay', 'thump', 'hangs', 'bliss', 'dealt', 'gains', 'bombs', 'clown', 'palms', 'cones', 'roast', 'tidal', 'bored', 'chant', 'acids', 'dough', 'camps', 'swore', 'lover', 'hooks', 'males', 'cocoa', 'punch', 'award', 'reins', 'ninth', 'noses', 'links', 'drain', 'fills', 'nylon', 'lunar', 'pulse', 'flown', 'elbow', 'fatal', 'sites', 'moths', 'meats', 'foxes', 'mined', 'attic', 'fiery', 'mount', 'usage', 'swear', 'snowy', 'rusty', 'scare', 'traps', 'relax', 'react', 'valid', 'robin', 'cease', 'gills', 'prior', 'safer', 'polio', 'loyal', 'swell', 'salty', 'marsh', 'vague', 'weave', 'mound', 'seals', 'mules', 'virus', 'scout', 'acute', 'windy', 'stout', 'folds', 'seize', 'hilly', 'joins', 'pluck', 'stack', 'lords', 'dunes', 'burro', 'hawks', 'trout', 'feeds', 'scarf', 'halls', 'coals', 'towel', 'souls', 'elect', 'buggy', 'pumps', 'loans', 'spins', 'files', 'oxide', 'pains', 'photo', 'rival', 'flats', 'syrup', 'rodeo', 'sands', 'moose', 'pints', 'curly', 'comic', 'cloak', 'onion', 'clams', 'scrap', 'didst', 'couch', 'codes', 'fails', 'ounce', 'lodge', 'greet', 'gypsy', 'utter', 'paved', 'zones', 'fours', 'alley', 'tiles', 'bless', 'crest', 'elder', 'kills', 'yeast', 'erect', 'bugle', 'medal', 'roles', 'hound', 'snail', 'alter', 'ankle', 'relay', 'loops', 'zeros', 'bites', 'modes', 'debts', 'realm', 'glove', 'rayon', 'swims', 'poked', 'stray', 'lifts', 'maker', 'lumps', 'graze', 'dread', 'barns', 'docks', 'masts', 'pours', 'wharf', 'curse', 'plump', 'robes', 'seeks', 'cedar', 'curls', 'jolly', 'myths', 'cages', 'gloom', 'locks', 'pedal', 'beets', 'crows', 'anode', 'slash', 'creep', 'rowed', 'chips', 'fists', 'wines', 'cares', 'valve', 'newer', 'motel', 'ivory', 'necks', 'clamp', 'barge', 'blues', 'alien', 'frown', 'strap', 'crews', 'shack', 'gonna', 'saves', 'stump', 'ferry', 'idols', 'cooks', 'juicy', 'glare', 'carts', 'alloy', 'bulbs', 'lawns', 'lasts', 'fuels', 'oddly', 'crane', 'filed', 'weird', 'shawl', 'slips', 'troop', 'bolts', 'suite', 'sleek', 'quilt', 'tramp', 'blaze', 'atlas', 'odors', 'scrub', 'crabs', 'probe', 'logic', 'adobe', 'exile', 'rebel', 'grind', 'sting', 'spine', 'cling', 'desks', 'grove', 'leaps', 'prose', 'lofty', 'agony', 'snare', 'tusks', 'bulls', 'moods', 'humid', 'finer', 'dimly', 'plank', 'china', 'pines', 'guilt', 'sacks', 'brace', 'quote', 'lathe', 'gaily', 'fonts', 'scalp', 'adopt', 'foggy', 'ferns', 'grams', 'clump', 'perch', 'tumor', 'teens', 'crank', 'fable', 'hedge', 'genes', 'sober', 'boast', 'tract', 'cigar', 'unite', 'owing', 'thigh', 'haiku', 'swish', 'dikes', 'wedge', 'booth', 'eased', 'frail', 'cough', 'tombs', 'darts', 'forts', 'choir', 'pouch', 'pinch', 'hairy', 'buyer', 'torch', 'vigor', 'waltz', 'heats', 'herbs', 'users', 'flint', 'click', 'madam', 'bleak', 'blunt', 'aided', 'lacks', 'masks', 'waded', 'risks', 'nurse', 'chaos', 'sewed', 'cured', 'ample', 'lease', 'steak', 'sinks', 'merit', 'bluff', 'bathe', 'gleam', 'bonus', 'colts', 'shear', 'gland', 'silky', 'skate', 'birch', 'anvil', 'sleds', 'groan', 'maids', 'meets', 'speck', 'hymns', 'hints', 'drown', 'bosom', 'slick', 'quest', 'coils', 'spied', 'snows', 'stead', 'snack', 'plows', 'blond', 'tamed', 'thorn', 'waits', 'glued', 'banjo', 'tease', 'arena', 'bulky', 'carve', 'stunt', 'warms', 'shady', 'razor', 'folly', 'leafy', 'notch', 'fools', 'otter', 'pears', 'flush', 'genus', 'ached', 'fives', 'flaps', 'spout', 'smote', 'fumes', 'adapt', 'cuffs', 'tasty', 'stoop', 'clips', 'disks', 'sniff', 'lanes', 'brisk', 'imply', 'demon', 'super', 'furry', 'raged', 'growl', 'texts', 'hardy', 'stung', 'typed', 'hates', 'wiser', 'timid', 'serum', 'beaks', 'rotor', 'casts', 'baths', 'glide', 'plots', 'trait', 'resin', 'slums', 'lyric', 'puffs', 'decks', 'brood', 'mourn', 'aloft', 'abuse', 'whirl', 'edged', 'ovary', 'quack', 'heaps', 'slang', 'await', 'civic', 'saint', 'bevel', 'sonar', 'aunts', 'packs', 'froze', 'tonic', 'corps', 'swarm', 'frank', 'repay', 'gaunt', 'wired', 'niece', 'cello', 'needy', 'chuck', 'stony', 'media', 'surge', 'hurts', 'repel', 'husky', 'dated', 'hunts', 'mists', 'exert', 'dries', 'mates', 'sworn', 'baker', 'spice', 'oasis', 'boils', 'spurs', 'doves', 'sneak', 'paces', 'colon', 'siege', 'strum', 'drier', 'cacao', 'humus', 'bales', 'piped', 'nasty', 'rinse', 'boxer', 'shrub', 'amuse', 'tacks', 'cited', 'slung', 'delta', 'laden', 'larva', 'rents', 'yells', 'spool', 'spill', 'crush', 'jewel', 'snaps', 'stain', 'kicks', 'tying', 'slits', 'rated', 'eerie', 'smash', 'plums', 'zebra', 'earns', 'bushy', 'scary', 'squad', 'tutor', 'silks', 'slabs', 'bumps', 'evils', 'fangs', 'snout', 'peril', 'pivot', 'yacht', 'lobby', 'jeans', 'grins', 'viola', 'liner', 'comet', 'scars', 'chops', 'raids', 'eater', 'slate', 'skips', 'soles', 'misty', 'urine', 'knobs', 'sleet', 'holly', 'pests', 'forks', 'grill', 'trays', 'pails', 'borne', 'tenor', 'wares', 'carol', 'woody', 'canon', 'wakes', 'kitty', 'miner', 'polls', 'shaky', 'nasal', 'scorn', 'chess', 'taxis', 'crate', 'shyly', 'tulip', 'forge', 'nymph', 'budge', 'lowly', 'abide', 'depot', 'oases', 'asses', 'sheds', 'fudge', 'pills', 'rivet', 'thine', 'groom', 'lanky', 'boost', 'broth', 'heave', 'gravy', 'beech', 'timed', 'quail', 'inert', 'gears', 'chick', 'hinge', 'trash', 'clash', 'sighs', 'renew', 'bough', 'dwarf', 'slows', 'quill', 'shave', 'spore', 'sixes', 'chunk', 'madly', 'paced', 'braid', 'fuzzy', 'motto', 'spies', 'slack', 'mucus', 'magma', 'awful', 'discs', 'erase', 'posed', 'asset', 'cider', 'taper', 'theft', 'churn', 'satin', 'slots', 'taxed', 'bully', 'sloth', 'shale', 'tread', 'raked', 'curds', 'manor', 'aisle', 'bulge', 'loins', 'stair', 'tapes', 'leans', 'bunks', 'squat', 'towed', 'lance', 'panes', 'sakes', 'heirs', 'caste', 'dummy', 'pores', 'fauna', 'crook', 'poise', 'epoch', 'risky', 'warns', 'fling', 'berry', 'grape', 'flank', 'drags', 'squid', 'pelts', 'icing', 'irony', 'irons', 'barks', 'whoop', 'choke', 'diets', 'whips', 'tally', 'dozed', 'twine', 'kites', 'bikes', 'ticks', 'riots', 'roars', 'vault', 'looms', 'scold', 'blink', 'dandy', 'pupae', 'sieve', 'spike', 'ducts', 'lends', 'pizza', 'brink', 'widen', 'plumb', 'pagan', 'feats', 'bison', 'soggy', 'scoop', 'argon', 'nudge', 'skiff', 'amber', 'sexes', 'rouse', 'salts', 'hitch', 'exalt', 'leash', 'dined', 'chute', 'snort', 'gusts', 'melon', 'cheat', 'reefs', 'llama', 'lasso', 'debut', 'quota', 'oaths', 'prone', 'mixes', 'rafts', 'dives', 'stale', 'inlet', 'flick', 'pinto', 'brows', 'untie', 'batch', 'greed', 'chore', 'stirs', 'blush', 'onset', 'barbs', 'volts', 'beige', 'swoop', 'paddy', 'laced', 'shove', 'jerky', 'poppy', 'leaks', 'fares', 'dodge', 'godly', 'squaw', 'affix', 'brute', 'nicer', 'undue', 'snarl', 'merge', 'doses', 'showy', 'daddy', 'roost', 'vases', 'swirl', 'petty', 'colds', 'curry', 'cobra', 'genie', 'flare', 'messy', 'cores', 'soaks', 'ripen', 'whine', 'amino', 'plaid', 'spiny', 'mowed', 'baton', 'peers', 'vowed', 'pious', 'swans', 'exits', 'afoot', 'plugs', 'idiom', 'chili', 'rites', 'serfs', 'cleft', 'berth', 'grubs', 'annex', 'dizzy', 'hasty', 'latch', 'wasps', 'mirth', 'baron', 'plead', 'aloof', 'aging', 'pixel', 'bared', 'mummy', 'hotly', 'auger', 'buddy', 'chaps', 'badge', 'stark', 'fairs', 'gully', 'mumps', 'emery', 'filly', 'ovens', 'drone', 'gauze', 'idiot', 'fussy', 'annoy', 'shank', 'gouge', 'bleed', 'elves', 'roped', 'unfit', 'baggy', 'mower', 'scant', 'grabs', 'fleas', 'lousy', 'album', 'sawed', 'cooky', 'murky', 'infer', 'burly', 'waged', 'dingy', 'brine', 'kneel', 'creak', 'vanes', 'smoky', 'spurt', 'combs', 'easel', 'laces', 'humps', 'rumor', 'aroma', 'horde', 'range', 'swiss', 'leapt', 'opium', 'slime', 'afire', 'pansy', 'mares', 'soaps', 'husks', 'snips', 'hazel', 'lined', 'cafes', 'naive', 'wraps', 'sized']

def black_on_gray(text):
    """Return text coloured black, with gray background. Remaining letters."""

    return "\033[0;30;47m"+text+"\033[0m"


def white_on_black(text):
    """Return text coloured white with black background. Not in word."""

    return "\033[5;37;40m"+text+"\033[0m"


def white_on_green(text):
    """Return text coloured white with green background. Correct Position."""

    return "\033[0;37;42m"+text+"\033[0m"

def white_on_yellow(text):
    """Return text coloured white with yellow background. In word, wrong position."""

    return "\033[0;37;43m"+text+"\033[0m"


def get_word(word_list):
    """Return a word randomly chosen from word_list."""

    return random.choice(word_list)

def print_list(lst: [str]):
    ''' Prints each element in <<list>> on a separate line. IF there is a list within a list, prints every individual value on a different line.
    >>> print_list(['hi', 'hello', 'bye']
    hi
    hello
    bye
    '''
    for elem in lst:
        if type(elem) != list:
            print(elem)
        else:
            print_list(elem)

def get_user_word(prompt, printed: [str]) -> str:
    ''' Gets a valid word from the user. If word is invalid, clears that guess. '''
    while True:
        print()
        guess = input(prompt).lower()
        if guess in WORDS:
            return guess.upper()
        else:
            print('Not a valid word')
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_list(printed)

def add_colours(letter_colours: dict, word:str) -> dict:
    ''' Adds a coloured word to a dictionary with letters and their corresponding colours as they should appear in the word bank.
    If a letter is coloured twice the one with the higher precedence takes its place. Order of precedence: Green, Yellow, Black
    '''
    list_of_char = word[:-1].split(' ')
    for i in range(0, 15, 3):
        # If the colour is green, it is immediately added to the letter_colours as green
        if list_of_char[i][8] == '2':
            letter_colours[list_of_char[i+1]] = list_of_char[i] + list_of_char[i+1] + list_of_char[i+2]
        elif list_of_char[i][8] == '3':
            if list_of_char[i+1] in letter_colours:
                # If the colour is not already green, it will change to yellow
                if '\033[0;37;42' not in letter_colours[list_of_char[i+1]]:
                    letter_colours[list_of_char[i+1]] = list_of_char[i] + list_of_char[i+1] + list_of_char[i+2]
            else:
                letter_colours[list_of_char[i+1]] = list_of_char[i] + list_of_char[i+1] + list_of_char[i+2]
        # if it is neither green now yellow, it will be black
        else:
            if list_of_char[i+1] not in letter_colours:
                letter_colours[list_of_char[i+1]] = list_of_char[i] + list_of_char[i+1] + list_of_char[i+2]
    return letter_colours

def change_colour(real_word:str, guess:str) -> str:
    ''' Returns the guess with the colours changed accordingly according to the wordle rules '''

    real_word_appearances = {real_word[0]: real_word.count(real_word[0]), real_word[1]: real_word.count(real_word[1]), real_word[2]: real_word.count(real_word[2]), real_word[3]: real_word.count(real_word[3]), real_word[4]: real_word.count(real_word[4])}
    right_place = {guess[0]:0, guess[1]:0, guess[2]:0, guess[3]:0, guess[4]:0}
    num_yellow = {guess[0]: 0, guess[1]: 0, guess[2]: 0, guess[3]: 0, guess[4]: 0}

    # Updates the dictionary with the number of times a letter is in the right place, and how mnay times it is yellow
    for i in range(5):
        if real_word[i] == guess[i]:
            right_place[guess[i]] += 1
    for i in range(5):
        if guess[i] in real_word_appearances:
            num_yellow[guess[i]] = real_word_appearances[guess[i]] - right_place[guess[i]]

    result = ''

    for i in range(5):
        if real_word[i] == guess[i]:
            result += white_on_green(' ' + guess[i] + ' ') + ' '
        # Determines if something is yellow using the num_yellow counter
        elif guess[i] in real_word_appearances and num_yellow[guess[i]] > 0:
            result += white_on_yellow(' ' + guess[i] + ' ') + ' '
            num_yellow[guess[i]] -= 1
        else:
            result += white_on_black(' ' + guess[i] + ' ') + ' '

    return result

def play_wordle() -> int:
    ''' Plays one round of the wordle game and returns the the number of guesses '''
    num_guesses = 0
    letter_bank = ''
    guessed = False
    real_word = get_word(WORDS).upper()

    # generates a letter bank (without any black, green, or yellow colours)
    letters = 'QWERTYUIOPn ASDFGHJKLn   ZXCVBNM'
    for char in letters:
        if char != ' ' and char != 'n':
            letter_bank += black_on_gray(char) + ' '
        elif char == 'n':
            letter_bank += '\n\n'
        else:
            letter_bank += char

    printed =  ['   -- Wordle! --',''] + [(black_on_gray('   ') + ' ') * 5, ''] * 6 + ['', letter_bank]
    print_list(printed)
    colours = {}

    while num_guesses < 6 and not guessed:
        user_guess = get_user_word('> ', printed)
        coloured_word = change_colour(real_word, user_guess)
        colours = add_colours(colours, coloured_word)
        # generates a letter bank with updated colours
        letter_bank = ''
        for char in letters:
            if char in colours:
                letter_bank += colours[char] + ' '
            elif char == 'n':
                letter_bank += '\n\n'
            elif char == ' ':
                letter_bank += char
            else:
                letter_bank += black_on_gray(char) + ' '

        printed[num_guesses * 2+2] = coloured_word
        printed[-1] = letter_bank
        if user_guess == real_word:
            guessed = True
        os.system('cls' if os.name == 'nt' else 'clear')        
        print_list(printed)
        num_guesses += 1
    if guessed:
        print()
        print('You won in {} guess(es)! \n'.format(num_guesses))
        global guess_distribution
        guess_distribution[num_guesses-1] += 1
        return num_guesses
    else:
        print()
        print('You lost! The word was {} \n'.format(real_word))
        return 0

user_status = input('Welcome to wordle! Do you know how to play (Y/N)? Press Q to exit! ').upper()
played = 0
guess_distribution = [0, 0, 0, 0, 0, 0]

cur_streak = 0
max_streak = 0

while user_status != 'Q':
    os.system('cls' if os.name == 'nt' else 'clear')
    if user_status == 'Y':
        guess_num = play_wordle()
        played += 1
        print('Statistics: \nPlayed: {}'.format(played))
        print('Win %: {}'.format(round(sum(guess_distribution) * 100/ played)))
        if guess_num:
            cur_streak += 1
            if cur_streak > max_streak:
                max_streak = cur_streak
        else:
            cur_streak = 0
        print('Current Streak: {}'.format(cur_streak))
        print('Max Streak: {}\n'.format(max_streak))
        print('Guess Distribution')
        for i in range(1,7):
            if i == guess_num:
                print(i, '🟦' * guess_distribution[i-1], '- ', guess_distribution[i-1])
            else:
                print(i, '⬛' * guess_distribution[i-1], '- ', guess_distribution[i-1])
        user_status = input('\nWould to play again (Y), see instructions (I) or quit (Q)? ').upper()

    elif user_status == 'N' or user_status == 'I':
        # Instructions
        print('HOW TO PLAY:\nGuess the Wordle in 6 Tries')
        print('\n- Each guess must be a valid 5-letter word.')
        print('- The color of the tiles will change to show how close your guess was to the word.\n')
        print('EXAMPLES')
        print(white_on_green('W') + black_on_gray(' E A R Y'))
        print('W is in the word and in correct spot.\n')
        print(black_on_gray('P ') + white_on_yellow('I') + black_on_gray(' L L S'))
        print('I is in the word but in the wrong spot.\n')
        print(black_on_gray('V A G ' + white_on_black('U') + black_on_gray(' E')))
        print('U is not in the word in any spot.')
        user_status = input('\nAre you ready to play (Y)? ').upper()
    else:
        user_status = input('That was not a valid response, try again! Do you know how to play (Y/N)? Press Q to exit! ').upper()

os.system('cls' if os.name == 'nt' else 'clear')
print('Thanks for playing!')

