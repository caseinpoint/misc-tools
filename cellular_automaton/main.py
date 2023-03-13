from automata import automata
from board import Board
from pprint import pprint
from subprocess import run
from sys import getsizeof
from time import sleep


def run_game(board, speed='m'):
    if speed == 'ss':
        sleep_duration = 0.5
    elif speed == 's':
        sleep_duration = 0.25
    elif speed == 'f':
        sleep_duration = 0.0625
    else:
        sleep_duration = 0.125

    run(['clear'])
    board.print_cells()

    while True:
        try:
            sleep(sleep_duration)

            board.tick()

            run(['clear'])
            board.print_cells()
            print(f'(press CTRL+C to stop) Generation: {board.generation}')

        except KeyboardInterrupt:
            print(' stopped')
            break


if __name__ == '__main__':
    from argparse import ArgumentParser
    from shutil import get_terminal_size

    arg_parser = ArgumentParser()
    arg_parser.add_argument('-r', '--random',
                            action='store_true',
                            help='create a randomly populated board')
    arg_parser.add_argument('-f', '--file',
                            help='create a board from a .csv file')
    arg_parser.add_argument('-a', '--alive',
                            help='character to be used for an "alive" cell',
                            default='█')
    arg_parser.add_argument('-d', '--dead',
                            help='character to be used for a "dead" cell',
                            default=' ')
    arg_parser.add_argument('-s', '--speed',
                            help='animation speed [s(low), m(edium), f(ast)]',
                            choices=['ss', 's', 'm', 'f'],
                            default='m')
    arg_parser.add_argument('--rule',
                            help='cellular automaton rule',
                            choices=list(automata.keys()),
                            default='life')
    args = arg_parser.parse_args()

    rule = automata[args.rule]

    if args.random:
        terminal = get_terminal_size()
        width = terminal.columns
        height = terminal.lines - 3

        board = Board.random_board(width=width,
                                   height=height,
                                   born=rule['born'],
                                   survive=rule['survive'],
                                   alive=args.alive,
                                   dead=args.dead)
    elif args.file is not None:
        board = Board.from_file(filename=args.file,
                                born=rule['born'],
                                survive=rule['survive'],
                                alive=args.alive,
                                dead=args.dead)
    else:
        arg_parser.error('-r or -f are required')

    run_game(board, args.speed)

    print('Average # live neighbors in 1st 10 generations:')
    pprint(board.live_neighbors_avgs[:10])

