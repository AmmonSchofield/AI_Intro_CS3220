class Actor:
  def __init__(self, id, name, birthday, corpus):
      self.actorID = id
      self.actorName = name
      self.actorBirthday = birthday
      self.actorShows = {}
      self.populateShows(corpus)
      self.relations = {}
      self.influence = 0

  # Properties

  @property
  def id(self): return self.actorID

  @property
  def name(self): return self.actorName

  @property
  def birthday(self): return self.actorBirthday

  # Property setters

  @id.setter
  def id(self, value): self.actorID = value

  @name.setter
  def name(self, value): self.actorName = value
  
  @birthday.setter
  def birthday(self, value): self.actorBirthday = value
  
  def addShow(self, showID, showDate):
      if showID and not (showID in self.actorShows):
          self.actorShows[showID] = showDate
  
  def populateShows(self, corpus):
      for show in corpus:
          for character in show['cast']:
              person = character['person']
              if self.id == person['id']:
                  self.addShow(show['id'], show['premiered'])

  def addRelation(self, actorID):
      if actorID and actorID != self.actorID:
            if actorID in self.relations:
                self.relations[actorID] += 1
            else:
                self.relations[actorID] = 1

  def computeRelations(self, graph):
      for actor in graph:
          for show in actor:
              if show in self.actorShows:
                  self.addRelation(actor.id)
      self.computeInfluence()
  
  def printRelations(self):
    for actorID, weight in self.relations.items():
      print(f"with {actorID}: {weight}")
  
  def computeInfluence(self):
      self.influence = sum(self.relations.values()) / len(self.relations)

  def __iter__(self):
      for show in self.actorShows:
          yield show
  
  def __contains__(self):
      if show in self.actorShows:
          return True
      else:
          return False
  
  def __str__(self):
      return f'The actor {self.actorID} has a name {self.actorName} and birthday {self.actorBirthday}'