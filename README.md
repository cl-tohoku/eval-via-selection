# Dialogue Response Selection Test Set with Well-Chosen False Candidates
This repository has the code to construct the response selection test set we developed in:

Shiki Sato, Reina Akama, Hiroki Ouchi, Jun Suzuki and Kentaro Inui. Evaluating Dialogue Generation Systems via Response Selection. [[arXiv]](https://arxiv.org/abs/2004.14302)

## Statistics
Below are statistics for the test set:
- Total questions: 1,019
- Candidates per question: 4
- Context turns per question: 3

## Construction
### 1. Prepare the OpenSubtitles data
This dataset uses movie and television subtitles data from OpenSubtitles. See http://opus.nlpl.eu/OpenSubtitles-v2018.php and the following citation:

> P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles. LREC 2016.

```
wget 'http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.en.gz' -O en.txt.gz
gunzip en.txt.gz
```

### 2. Prepare the DailyDialog data
This dataset uses multi-turn dialog data from OpenSubtitles. See http://yanran.li/dailydialog and the following citation:

> Yanran Li, Hui Su, Xiaoyu Shen, Wenjie Li, Ziqiang Cao, and Shuzi Niu. DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset. IJCNLP 2017.

```
wget 'http://yanran.li/files/ijcnlp_dailydialog.zip' ijcnlp_dailydialog.zip
unzip ijcnlp_dailydialog.zip
```

### 3. Extract the utterances
```
bash create_test.sh ijcnlp_dailydialog/dialogues_text.txt en.txt [TestsetName]
rm tmp_1 tmp_2
``` 

## Format
Each line of [TestsetName] corresponds to a response selection question. Utterances are splitted by "\t".

```
[utterence1_of_context]\t[utterence2_of_context]\t[utterence3_of_context]\t
[Ground_Truth]\t[false_candidate1]\t[false_candidate2]\t[false_candidate3]
```

## Human Evaluation Scores
If you need human evaluation scores for the test set candidates (see Section 3.1 of our paper), please refer to `human_scores.jsonl`.
The record in the $n$-th line of `human_scores.jsonl` contains human scores for candidates of the question in the $n$-th line of [TestsetName]. The format is as follows:

```
[
 [score_for_Ground_Truth_by_human1,
  score_for_Ground_Truth_by_human2,
  ...,
  score_for_Ground_Truth_by_human5
 ],
 [score_for_false_candidate1_by_human1,
  score_for_false_candidate1_by_human2,
  ...,
  score_for_false_candidate1_by_human5
 ],
 [score_for_false_candidate2_by_human1,
  ...,
 ],
 [score_for_false_candidate3_by_human1,
  ...,
  score_for_false_candidate3_by_human5
 ]
]
```

## Citation
If you use this test set, please cite the following:

> Shiki Sato, Reina Akama, Hiroki Ouchi, Jun Suzuki and Kentaro Inui. Evaluating Dialogue Generation Systems via Response Selection. In Proceedings of the 58th annual meeting of the Association for Computational Linguistics (ACL 2020), July 2020.
