HANGMAN_TITLE = """██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                    a game by OsvaJorge"""

SUBMENU = """
        __                                            
        / _       _  _  _   |_ |_   _        _   _  _| 
        \__) |_| (- _) _)   |_ | ) (-   \)/ (_) |  (_| 
                                                                                            
    """

STATEGES = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

#This one is not in use, maybe it will in later versions
alphabet = {
    'a': '▄▀█\n█▀█',
    'b': '█▄▄\n█▄█',
    'c': '█▀▀\n█▄▄',
    'd': '█▀▄\n█▄▀',
    'e': '█▀▀\n██▄',
    'f': '█▀▀\n█▀░',
    'g': '█▀▀\n█▄█',
    'h': '█░█\n█▀█',
    'i': '░█░\n░█░',
    'j': '░░█\n█▄█',
    'k': '█▄▀\n█░█', 
    'l': '█░░\n█▄▄',
    'm': '╔╗╗\n║║║',
    'n': '▄▄▄\n█ █',
    'o': '█▀█\n█▄█',
    'p': '█▀█\n█▀▀',
    'q': '█▀█\n▀▀█',
    'r': '█▀█\n█▀▄',
    's': '█▀░\n▄█░',
    't': '▀█▀\n░█░',
    'u': '█░█\n█▄█',
    'v': '█░█\n▀▄▀',
    'w': '║║║\n╚╝╝',
    'x': '▀▄▀\n█░█',
    'y': '█▄█\n░█░',
    'z': '▀█░\n█▄░'
}