#LAYERS
# Background
# Layer 1 - background of building
# Layer 2 - interactables and cosmetics
# Layer 3 - collidables with player

#LEGEND
#
# P = Player
# F = Floor
# R = Roof
# C = Cracked wall
# D = Death block
# L = Lava
# S = Stair
# W = Wall
# T = Trap


level_map_1 = [
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                                                                                              BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBB; XXXXXXXXXXXXXXXXXXXXXXX BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                                                BBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBB;BYXXXXXXXXXXXXXXXXXXXXXXX  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBB;BYXXXXXXXXXXXXXXXXXXXXXXXXXXBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
';                  BYXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXX BBB XXX BBB XXX BBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
' YIIIIIIIIIIK&HIIIIIXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             XBX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                     ',
' VXRO123XQXXJ~LXRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX B XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
' VOFX4 5XAXOM^NXFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX B XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
' VXCX6 7OTXXJ0GXCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'(                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX X XXXXXXX X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx',
'BBBBBBBBBBBBBBBBBBB( XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX B XXXXXXX B XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                 XXXXXXXXXX          ',
'BBBBBBBBBBBBBBBBBBBB(  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XBX       XBX                 XXX     XXX     XXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX9BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXX BBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXXXX       BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXX BBB XXX BBB XXX BBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX9BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXX BBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXX  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXX BBB XXX BBB XXX BBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX9BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXX BBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXX BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXX BBB XXX BBB XXX BBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX BBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX9BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXX BBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBBB( XX                 XX )BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBXXXBBBBBXXXBBBBBXXXBBBBBBBB                                                BBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX9BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXX BBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX9BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXX BBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX9BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXX BBBBBBBBBB',
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XXXXXXXX XXXXXXXXXX',
'                                                                                                                                                                                                                                                                                                                          XXXXXXXX           ',
'                                                                                                                                                                                                                                                                                                                          XXXXXXXX           ',
'                                                                                                                                                                                                                                                                                                                          XXXXXXXX           ',
'                                                                                                                                                                                                                                                                                                                          XXXXXXXX           ',
'                                                                                                                                                                                                                                                                                                                          XXXXXXXX           ',
'                                                                                                                                                                                                                                                                                                                          XXXXXXXX           ',
'                                                                                                                                                                                                                                                                                                                          XXXXXXXX           ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',                                                                                                                                                                                                                                                           
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXSXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  XXXXXXXXXXXXXXXXXXXXXXXX   ',
'                                                                                                                                                                                                                                                                                                                  [----------------------]   ',
'                                                                                                                                                                                                                                                                                                                                             ']

level_map_2 = [
'                                                                                                                                                                         ______________________________________________________________________________________________                                                                      ',
'                      _DDDDDDDDDDDDDDDDDDDDDDD_                                                                   ________________________________________________      8                                                                                              9                                                                     ',
'                     /                         9                                                                 8                                                9     8                                                                                              9                                                                     ',
'                    /                          |                                                                 8                                                9     8                                                                                              9                                                                     ',
' __________________/                            9                                      DDD     DDD     DDD       8                                                9     8                                                                                              9                                                                     ',
'8                                               |_____________   _____DDDDDDDDDDDDDDDD/   |DDD/   |DDD/   |DDDDDD/                                                |_____/                                                                                              |_____________________________________________________________________',
'8                      E           <=>    E                   9 8                                                    <================>    <=======>   <======>                                                                                                                                                                              ',
'8          ?          <==>              <==>                  9 8                                                                                                                                <=====>                                                                                                                                     ',
'8     P                       <=>                             |D/                                                                                                                      <====>                                                          <====>                                                                                ',
' ------------------]                                     [U]       [U]                                                                                                      <=====>                          <======>                <====>   <====>           <==>                                                                          ',
'                    ]                                    9 8       9 8                                               <===========>    <=====>   <=============>                                                           <=====>                                      [-------------------------------------------------]        [----------', 
'                     -]   <==>        E                [-   -------   ----------------]   [---]   [---]   [------]                                                [-----]                                                                                              9                                                 8        9          ',
'                      8>             <==>       [------                               8   9   8   9   8   9      8                                                9     8                                                                                              9                                                 8        9          ',
'                      8                       [-                                      8   9   8   9   8   9      8=>                                            <=9     8                                                                                              9                                                 8        9          ',
'                      8      E  E   E E      <9                                       8   9   8   9   8   9      8                                                9     8                                                                                              9                                                 8        9          ',
'                       ]UU[---------------]UU[                                         UUU     UUU     UUU        ------------------------------------------------      8                                                                                              9                                                 8        9          ',
'                                                                                                                                                                        8                                                                                              9                                                 8        9          ',
'                                                                                                                                                                        8                                                                                              9                                                 8        9          ',
'                                                                                                                                                                        8UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU9                                                 8        9          ',
'                                                                                                                                                                                                                                                                                                                         8        9          ',
'                                                                                                                                                                                                                                                                                                                         8        9          ',
'                                                                                                                                                                                                                                                                                                                         8        9          ',
'                                                                                                                                                                                                                                                                                                                         8        9          ',
'                                                                                                                                                                                                                                                                                                                         8        9          ',
'                                                                                                                                                                                                                                                                                                                         8        9          ',
'                                                                                                                                                                                                                                                                                                                         8        9          ',
'                                                                                                                                                                                                                                                                                                                  DDDDDDD/        |DDDDDDD   ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',                                                                                                                                                                                                                                                           
'                                                                                                                                                                                                                                                                                                                 8            S           9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                 8                        9  ',
'                                                                                                                                                                                                                                                                                                                  [----------------------]   ',
'                                                                                                                                                                                                                                                                                                                                             ']

level_map = [level_map_1, level_map_2]

tile_size = 32
screen_width = 1080
screen_height = 19 * tile_size




