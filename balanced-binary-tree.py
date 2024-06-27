def isbalanced(root)-> bool:
    balanced = [True]
    
    def height(root):
        if not root:
            return 0
        
        left = height(root.left)
        right = height(root.right)
        
        if abs(left-right) >1:
            balanced[0] = False
            return 0
        
    height(root)
    return balanced[0]