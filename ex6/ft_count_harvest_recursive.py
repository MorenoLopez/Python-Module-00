#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/08 10:15:39 by horarivo            #+#    #+#            #
#   Updated: 2026/04/08 10:15:41 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive(n=None, day=1) -> None:
    if n is None:
        n = int(input("Days until harvest: "))
    if day > n:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(n, day + 1)
