import re

format = 'dude-thats-my-ghost'
title = 'Dude,-That\'s-My-Ghost!'

title = re.sub(',', '', title)
title = re.sub('\'', '', title)
title = re.sub('!', '', title)

print(title)

