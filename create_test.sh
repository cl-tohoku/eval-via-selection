python3 process_dailydialog.py $1 indice/dailydialog.txt tmp_1
python3 process_opensubtitles.py $2 indice/opensubtitles.txt tmp_2
python3 merge_context_cands.py tmp_1 tmp_2 $3
