import argparse

def load_idx(idx_fname):
    indice_list = []
    indice = []
    with open(idx_fname) as idx_file:
        for l in idx_file:
            indice_in_l = [int(idx) for idx in l.strip().split("\t")]
            indice_list.append(indice_in_l)
            indice.extend(indice_in_l)
    return indice_list, set(indice)

def load_opensubtitles(in_fname, indice):
    id2txt = {}
    with open(in_fname) as in_file:
        for idx,l in enumerate(in_file):
            if idx in indice:
                id2txt[idx] = l.strip()
    return id2txt

def write_txt(indice_list, id2txt, out_fname):
    with open(out_fname,"w") as out_file:
        for indice in indice_list:
            out_file.write("{}\n".format("\t".join([id2txt[idx] for idx in indice])))

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_fname")
    parser.add_argument("idx_fname")
    parser.add_argument("out_fname")
    args = parser.parse_args()

    indice_list, indice = load_idx(args.idx_fname)
    id2txt = load_opensubtitles(args.in_fname, indice)
    write_txt(indice_list, id2txt, args.out_fname)
