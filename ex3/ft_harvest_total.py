#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/08 10:15:07 by horarivo            #+#    #+#            #
#   Updated: 2026/04/22 19:56:25 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total() -> None:
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day1 + day2 + day3}")
