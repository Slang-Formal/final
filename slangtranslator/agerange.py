

def agePrediction(string):
    low_dict = {"ded", "spoopy","blankie", "tummyache", "tummy ache", "ouchie", "sippy cup", "potty","binky", "boo boo", "boo-boo", "tummy", "yucky", "no no", "no-no", "blankey", "wawa", "nigh-nigh", "nigh nigh", "nini", "nuggies","uwu", "dank","catch feelings", "caught feelings", "normie", "moots", "baller", "sigma", "alpha", "fleek", "bff", "stan", "noob", "bae", "simp", "simping", "sus", "squad", "shook", "salty", "AF", "lit", "unalive", "clutch", "boi", "based", "rizz", "shading", "shade", "weaboo"}
    mid_dict = { "goofy", "GOAT", "gucci", "yeet", "mood", "lit", "stan", "clout", "vibe", "vibes", "FOMO","IRL", "TBH", "salty", "savage", "periodt","bruh", "bro", "dude", "chad", "zoomies", "L+ratio", "L + ratio", "caucacity", "lovebomb", "tripping", "trippin", "crunk", "flex", "cap", "bop", "chillax", "periodt","bruh", "yassify", "slay", "highk" "highkey", "lowkey","boomer", "lowk", "ONG", "go off", "tea", "flex", "ghosted", "ghosting", "woke", "bro", "fam", "glow up", "cancel culture", "eboy", "egirl","e-boy", "e-girl", "ghosting", "boujee", "finna", "cheugy", "smexy", "clapback", "snacc", "full send", "clutch", "ratchet", "brazy", "deadass", "based", "quid pro quo", "bars", "bih", "bussin", "cake", "dope", "drip", "facts", "finsta", "fire", "gas", "gtg", "hits different", "hits diff", "turnt", "LOL", "LMAO", "mid","xtra", "woe is me", "mami", "fav", "netflix and chill", "plug", "rizz", "smash", "zaddy","yuge","poppin", "oppa", "thirsty", "snatched", "extra", "adulting", "side eye", "ride or die"}
    high_dict = {"golly", "darn","fuddy-duddy", "hooey", "cat's pajamas", "rad", "righteous", "bee's knees", "foxy", "cool cat", "gee whiz", "gobbledygook", "hooey", "jive", "sock hop", "whippersnapper", "juke joint", "ducky", "g-man", "saddle shoes", "groovy", "far out", "goofy", "cool beans", "bummer", "hippy", "peace", "hang loose", "right on", "hotsy-totsy","tots", "rugrats", "mini-me's", "ankle-biters", "throuple","bell end", "brigading", "brigade", "adorkable", "food coma", "iykyk", "sup", "yadda", "GOAT","wassup", "diss", "newbie", "hangry", "buzzkill", "dibs", "quid pro quo", "ROFL"}


    low = 0 # Ages under 18
    mid = 0 # Ages 18-29 
    high = 0 # Ages 30 and up
    text = string.split(" ")
    for word in text:
        if word in low_dict:
            low += 1
        elif word in mid_dict:
            mid += 1
        elif word in high_dict:
            high += 1
        else:
            pass
        
    if max(low, mid, high) == low:
        return "0-18"
    elif max(low, mid, high) == mid:
        return "18-29"
    elif max(low, mid, high) == high:
        return "30+"
    else:
        return "Age range could not be determined"
    
