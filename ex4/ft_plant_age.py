#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/08 10:15:19 by horarivo            #+#    #+#            #
#   Updated: 2026/04/08 10:15:55 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age() -> None:
    if (int(input("Enter plant age in days: ")) <= 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
