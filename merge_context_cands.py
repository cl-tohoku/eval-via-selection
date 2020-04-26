import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("context_fname")
    parser.add_argument("candidates_fname")
    parser.add_argument("out_fname")
    args = parser.parse_args()

    with open(args.context_fname) as context_file,\
            open(args.candidates_fname) as candidates_file,\
            open(args.out_fname,"w") as out_file:
        for context, candidates in zip(context_file, candidates_file):
            if len(candidates.strip().split("\t")) >= 4:
                out_file.write("{}\t{}\n".format(
                    "\t".join(context.strip().split("\t")[:3]), candidates.strip()))
            else:
                out_file.write("{}\t{}\n".format(
                    context.strip(), candidates.strip()))
