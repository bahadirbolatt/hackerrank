""""
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   listcomprensions.py                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bbolat <bbolat@student.42kocaeli.com.tr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/02/07 13:54:57 by bbolat            #+#    #+#             */
/*   Updated: 2022/03/22 14:28:34 by bbolat           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
"""
x,y,z,n = [int(input()) for i in range(4)]
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])
