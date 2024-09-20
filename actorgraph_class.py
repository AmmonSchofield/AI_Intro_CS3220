from actor_class import Actor

class ActorGraph:
    def __init__(self, corpus):
        #initialisation of dictionary that will store all shows. They keys are the IDs, the values are Show objects.
        self.actors = {}
        self.corpus = corpus
        #Load the show corpus
        for data_show in corpus:
            cast = data_show['cast']
            for character in cast:
                person = character['person']
                if person['id'] not in self.actors:
                    actor = Actor(person['id'], person['name'], person['birthday'], corpus)
                    self.actors[actor.id] = actor

    def __iter__(self):
        for actor in self.actors.values():
            yield actor

    #Compute relations between users
    def buildRelations(self):
        for actor in self:
            actor.computeRelations(self)