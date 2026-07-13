#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/08 10:15:24 by horarivo            #+#    #+#            #
#   Updated: 2026/04/08 10:15:29 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder() -> None:
    if (int(input("Day since last watering: ")) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
