# # Sometimes the red tapes may be detected as "red cubes". 
# # So we need to exclude these areas that the red tapes fall.

import points as pts
from inQuadrilateralArea import inQuadrilateralArea

def inInvalidAreas(testPoint):

    in_tape_A = inQuadrilateralArea(pts.tape_A_LBPoint, 
                                    pts.tape_A_LTPoint, 
                                    pts.tape_A_RTPoint, 
                                    pts.tape_A_RBPoint, 
                                    testPoint)
    
    in_tape_B = inQuadrilateralArea(pts.tape_B_LBPoint, 
                                    pts.tape_B_LTPoint, 
                                    pts.tape_B_RTPoint, 
                                    pts.tape_B_RBPoint, 
                                    testPoint)

    in_tape_C = inQuadrilateralArea(pts.tape_C_LBPoint, 
                                    pts.tape_C_LTPoint, 
                                    pts.tape_C_RTPoint, 
                                    pts.tape_C_RBPoint, 
                                    testPoint)

    in_tape_D = inQuadrilateralArea(pts.tape_D_LBPoint, 
                                    pts.tape_D_LTPoint, 
                                    pts.tape_D_RTPoint, 
                                    pts.tape_D_RBPoint, 
                                    testPoint)

    in_tape_E = inQuadrilateralArea(pts.tape_E_LBPoint, 
                                    pts.tape_E_LTPoint, 
                                    pts.tape_E_RTPoint, 
                                    pts.tape_E_RBPoint, 
                                    testPoint)

    in_tape_F = inQuadrilateralArea(pts.tape_F_LBPoint, 
                                    pts.tape_F_LTPoint, 
                                    pts.tape_F_RTPoint, 
                                    pts.tape_F_RBPoint, 
                                    testPoint)

    if in_tape_A or in_tape_B or in_tape_C or in_tape_D or in_tape_E or in_tape_F: 
        return True # if the testPoint falls in one of the tape areas, returns True.
    else:
        return False # else returns True.