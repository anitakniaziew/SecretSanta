# -*- coding: utf-8 -*-

import random
import messaging
import persistence

from secrets import persons

pairs = {}
names = list(persons)

length = len(names)

random.shuffle(names)

# choosing pairs giver -> receiver
for i in range(0, length):
    pairs[names[i]] = names[(i+1) % length]

# backing up  results
persistence.save(pairs)

# sending messages to all givers
for giver in pairs:
    receiver = pairs[giver]
    phone = persons[giver]
    message = "Witamy, Ministerstwo Wesołych Świąt wylosowało Ci osobę " + \
        "do obdarowania prezentem w te Święta. Osobą tą jest: " + receiver + ". " + \
        "Przypominamy: wartość prezentu do 30 zł, nikomu nie zdradzamy kogo wylosowaliśmy. Powodzenia!"
    messaging.send(phone, message)
