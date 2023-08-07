import json
import numpy as np
import trimesh
from pathlib import Path
import os

def save_results(mesh_path):

    # segment_colors = np.array([[226, 24, 24],
    #             [112,206,78],
    #             [148,75,208],
    #             [201,209,80],
    #             [255, 140, 50],
    #             [104,207,153],
    #             [202,77,145],
    #             [86,109,55],
    #             [159,144,205],
    #             [197,137,55],
    #             [120,185,198],
    #             [100,46,49],
    #             [200,199,155],
    #             [58,71,80],
    #             [195,135,126]])
    
    segment_colors = np.array([
    [0, 114, 189],#0072BD
    [217, 83, 26],#D9531A
    [238, 177, 32],#EEB120
    [126, 47, 142],#7E2F8E
    [117, 142, 48],#758E30
    [76, 190, 238],#4CBEEE
    [162, 19, 48],#A21330
    [240, 166, 202]])#F0A6CA
    # if not os.path.exists('results'):
        # os.mkdir('results')

    output_path = mesh_path+"/"+"colored"
    if not os.path.exists(output_path):
        os.makedirs(output_path)


    for i,filename in enumerate(os.listdir(mesh_path)):
        input = os.path.join(mesh_path, filename)
        if os.path.isfile(input) :
            if os.path.splitext(input)[1] == ".obj" :
                input = input.replace("\\","/")
                preds_file = input.replace(".obj",".json")

                

                with open(preds_file) as f:
                    segment = json.load(f)
                
                mesh_name = input
                mesh = trimesh.load_mesh(mesh_name,force='mesh', process=False)       
                preds = ""         
                preds = np.array(segment['sub_labels']) 
                output_path_ =Path(output_path)

                print(mesh.faces.shape,preds.shape)
                while preds.shape[0] < mesh.faces.shape[0] :
                    preds = np.append(preds,0)

               
                
                mesh.visual.face_colors[:, :3] = segment_colors[preds[:mesh.faces.shape[0]]]
                mesh.export(output_path_ / f'pred-{Path(filename).stem}.ply')
                t = output_path+ "/" +f'pred-{Path(filename).stem}.ply'
                
                print(input,preds_file," ==> ",t,"\n\n")
    
    # preds_file = ""

    

    # print("saved at:"+t)

save_results("clr/")