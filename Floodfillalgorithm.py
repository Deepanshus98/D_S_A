#From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
#by a path of the same color as the starting pixel are colored with the new color.
#Note the bottom corner is not colored 2, because it is not 4-directionally connected
#to the starting pixel.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if(image[sr][sc]==newColor):
            return image
        old=image[sr][sc]
        stack=[(sr,sc)]
        while(stack):
            i,j=stack.pop()
            if(image[i][j]==old):
               image[i][j]=newColor    
               if(i+1<len(image)):
                  stack.append((i+1,j))
               if(i-1>=0):
                  stack.append((i-1,j))
               if(j+1<len(image[0])):
                  stack.append((i,j+1))
               if(j-1>=0):
                  stack.append((i,j-1))
            else:
               pass
        return image
