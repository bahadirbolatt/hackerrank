""""
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printfunction.py                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bbolat <bbolat@student.42kocaeli.com.tr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/02/07 13:54:57 by bbolat            #+#    #+#             */
/*   Updated: 2022/03/22 14:28:34 by bbolat           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
"""
#bu kod inputa girilen rakam kadar ekrana sayı bastırır.

N = int(input("sayi girin:"))
for i in range(1, N+1):
    print(i, end="") # 'end=""' yazmazsak her numara diğer satıra geçer.