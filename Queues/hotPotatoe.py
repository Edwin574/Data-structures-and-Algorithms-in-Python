'''In this game (see Figure 3.13) children line up in a circle and pass an item from
neighbour to neighbour as fast as they can. At a certain point in the game, the action is stopped
and the child who has the item (the potato) is removed from the circle. Play continues until
only one child is left.'''

from Queue import Queue
def hot_potatoe(name_list,num):
    game_queue=Queue()

    for name in name_list:
        game_queue.enqueue(name)

        while game_queue.size()>1:
            for i in range(num):
                print(f"{i}")
                game_queue.enqueue(game_queue.dequeue())
                # print(f'{i}')

            game_queue.dequeue()
        return game_queue.dequeue()
    
print(hot_potatoe(['Glen','Nell','Ivy','Pete','Edu','Bree'],7))

