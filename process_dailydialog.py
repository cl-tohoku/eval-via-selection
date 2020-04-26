import argparse

def load_idx(idx_fname):
    idx_list = []
    with open(idx_fname) as idx_file:
        for l in idx_file:
            idx_list.append(int(l.strip()))
    return idx_list

def load_dailydialog(in_fname, indice):
    id2txt = {}
    with open(in_fname) as in_file:
        for idx,l in enumerate(in_file):
            if idx in indice:
                utterances = [utterance.replace(" __eou__","") for utterance
                        in l.strip().split(" __eou__ ")]
                id2txt[idx] = "\t".join(utterances[:4])
    return id2txt

def write_txt(idx_list, id2txt, out_fname):
    with open(out_fname,"w") as out_file:
        for idx in idx_list:
            out_file.write("{}\n".format(id2txt[idx]))

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_fname")
    parser.add_argument("idx_fname")
    parser.add_argument("out_fname")
    args = parser.parse_args()

    idx_list = load_idx(args.idx_fname)
    indice = set(idx_list)
    id2txt = load_dailydialog(args.in_fname, indice)
    write_txt(idx_list, id2txt, args.out_fname)
