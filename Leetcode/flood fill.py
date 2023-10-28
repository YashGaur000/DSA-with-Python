class Solution:
    def floodfill(self, image, sr, sc, color):
        starting_pixel=image[sr][sc]

        self.dfs(image, sr, sc, color, starting_pixel)

        return image
    
    def dfs(self, image, sr, sc, color, starting_pixel):
        if sr<0 or sr>len(image)-1 or sc<0 or sc>len(image[0])-1 or image[sr][sc] == color or image[sr][sc] != starting_pixel:
            return 
        starting_pixel[sr][sc] = color
        self.dfs(starting_pixel, sr+1, sc, color, starting_pixel)
        self.dfs(starting_pixel, sr-1, sc, color, starting_pixel)
        self.dfs(starting_pixel, sr, sc+1, color, starting_pixel)
        self.dfs(starting_pixel, sr, sc-1, color, starting_pixel)


class Solution:
    def floodfill(self, image, sr, sc, color):
        starting_pixel = image[sr][sc]
        self.dfs(image, sr, sc, color, starting_pixel)
        return image
    
    def dfs(self, image, sr, sc, new_color, starting_pixel):
        if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] == new_color or image[sr][sc] != starting_pixel):
            return
        old_color = image[sr][sc]
        image[sr][sc] = new_color
        self.dfs(image, sr + 1, sc, new_color, old_color)
        self.dfs(image, sr - 1, sc, new_color, old_color)
        self.dfs(image, sr, sc + 1, new_color, old_color)
        self.dfs(image, sr, sc - 1, new_color, old_color)
 