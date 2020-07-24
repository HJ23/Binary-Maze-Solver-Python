
# Node for A* algorithm each node has 3 distance measure 2 simple 1 compound. 
class Node(object):
   def __init__(self,point):
      self.f=None
      self.h=None
      self.g=None
      self.point=point
      self.parent=None
   def __eq__(self,obj):
      return self.point==obj.point


# Algorithm starts here

class Astar(object):
   def __init__(self,start,end):
      self._start=start
      self._end=end

   def hDistance(self,point):
      return (point[0]-self._end[0])**2+(point[1]-self._end[1])**2

   def start(self,maze):

      # initialize start and end coordinates 

      start_node=Node(self._start)
      end_node=Node(self._end)

      start_node.f=start_node.g=start_node.h=0
      end_node.f=end_node.h=end_node.g=0
      
      open_nodes   =[start_node]
      closed_nodes =[]

      
      while(len(open_nodes)>0):
         current_node=open_nodes[0]
         index_node=0
         # check node has shorter distance ? if yes then current node is that one.
         for index,item in enumerate(open_nodes):
            if(item.f<current_node.f):
               current_node=item
               index_node=index
         open_nodes.pop(index_node)
         closed_nodes.append(current_node)
         
         # if end coordinates matches then return 
         if(current_node==end_node):
            path=[]
            tmp=current_node
            while(tmp is not None):
               path.append(tmp.point)
               tmp=tmp.parent
            return path[::-1]
         
         # move left right up and down and add nodes

         children=[]
         for move in [(0,1),(-1,0),(0,-1),(1,0)]:
             node_pos=(current_node.point[0]+move[0],current_node.point[1]+move[1])
             if((node_pos[0]>=len(maze) or node_pos[0]<0 or node_pos[1]<0 or node_pos[1]>=len(maze[0]))) :
                continue
             if(maze[node_pos[0]][node_pos[1]]==0):
                continue
             new_node=Node(node_pos)
             new_node.parent=current_node
             children.append(new_node)
         
         # refresh node distance and add open_nodes list
         for child in children:
             if(child in closed_nodes):
                continue
             else:
                child.g=current_node.g+1
                child.h=self.hDistance(child.point)
                child.f=child.g+child.h
                open_nodes.append(child)


