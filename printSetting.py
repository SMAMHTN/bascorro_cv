import rw_file as rw

daftar = {
    "l_h_gawang" : str(rw.read("setting/LH.txt")),
    "l_s_gawang" : str(rw.read("setting/LS.txt")),
    "l_v_gawang" : str(rw.read("setting/LV.txt")),
    "u_h_gawang" : str(rw.read("setting/UH.txt")),
    "u_s_gawang" : str(rw.read("setting/US.txt")),
    "u_v_gawang" : str(rw.read("setting/UV.txt")),

    "dilation_gawang" : str(rw.read("setting/dilation_gawang.txt")),
    "dilation_iteration_gawang" : str(rw.read("setting/dilation_iteration_gawang.txt")),
    
    "erosion_gawang" : str(rw.read("setting/erosion_gawang.txt")),
    "erosion_iteration_gawang" : str(rw.read("setting/erosion_iteration_gawang.txt")),
    
    "gaussian_gawang" : str(rw.read("setting/gaussian_gawang.txt")),
    
    "radius_gawang" : str(rw.read("setting/radius_gawang.txt")),

    "l_h_bola": str(rw.read("setting/LH.txt")),
    "l_s_bola": str(rw.read("setting/LS.txt")),
    "l_v_bola": str(rw.read("setting/LV.txt")),
    "u_h_bola": str(rw.read("setting/UH.txt")),
    "u_s_bola": str(rw.read("setting/US.txt")),
    "u_v_bola": str(rw.read("setting/UV.txt")),

    "dilation_bola": str(rw.read("setting/dilation_bola.txt")),
    "dilation_iteration_bola": str(rw.read("setting/dilation_iteration_bola.txt")),

    "erosion_bola": str(rw.read("setting/erosion_bola.txt")),
    "erosion_iteration_bola": str(rw.read("setting/erosion_iteration_bola.txt")),

    "gaussian_bola": str(rw.read("setting/gaussian_bola.txt")),

    "radius_bola": str(rw.read("setting/radius_bola.txt")),

}

for x in daftar.items():
    print (x)
