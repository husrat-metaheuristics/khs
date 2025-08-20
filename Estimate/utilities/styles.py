from reportlab.lib import colors
class style:
    TEXT_ALIGN_CENTER=(
        'ALIGN',(0,0),(-1,-1),'CENTER'
    )
    TEXT_ALIGN_RIGHT=(
        'ALIGN',(0,0),(-1,-1),'RIGHT'
    )
    TEXT_ALIGN_LEFT=(
        'ALIGN',(0,0),(-1,-1),'LEFT'
    )
    BOTTOM_PADDING_ALL_ZERO=(
        'BOTTOMPADDING',(0,0),(-1,-1),0
    )
    TOP_PADDING_ALL_ZERO=(
        'BOTTOMPADDING',(0,0),(-1,-1),0
    )
    LEFT_PADDING_ALL_ZERO=(
        'LEFTPADDING',(0,0),(-1,-1),0
    )
    RIGHT_PADDING_ALL_ZERO=(
        'RIGHTPADDING',(0,0),(-1,-1),0
    )

    VALIGN_ALL=(
         'VALIGN', (0,0), (-1,-1), 'TOP'
    )
    GRID_ALL=(
        'GRID',(0,0),(-1,-1),0.50,colors.black
    )
