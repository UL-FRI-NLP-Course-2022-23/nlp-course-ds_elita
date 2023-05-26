# Natural language processing course 2022/23: `Project 3: Paraphrasing sentences`

Group public acronym/name: `DS-elita`

Link to the report: [nlp_project.pdf](report/nlp_project.pdf)

## Data
The translated dataset is a subset of the [ParaBank2](https://nlp.jhu.edu/parabank/) dataset (first 100.000 rows) and can be downloaded [here](https://unilj-my.sharepoint.com/:u:/g/personal/kv4582_student_uni-lj_si/Efaka4o7MGJOilz7colF34EB039AxbwfpCtDRaJx_DoCKg?e=JC9vSB).

Dataset processing code can be found in src/translations. Translations were done with the Slovene NMT model available [here](https://github.com/clarinsi/Slovene_NMT).


## Fine-tuning the sloGPT model
We used the pretrained large language model [GPT-sl-base](https://huggingface.co/cjvt/gpt-sl-base) and finetuned it on the dataset generated above. The finetuning code can be found in [finetune-slo-paraphrase-gpt.ipynb](src/finetune-slo-paraphrase-gpt.ipynb). 

The model was finetuned for 3 epochs with a batch size of 16 and a learning rate of 5e-5. The model was trained on Kaggle, on a double Tesla T4 GPU with 16GB of memory.

The model was evaluated at **two checkpoints**: after 1.23 epochs and after 1.65 epochs.
The first checkpoint was chosen because the training loss was still dropping and the second checkpoint was chosen because the training loss was starting to increase again.

 - For the first checkpoint the model is available [here](https://drive.google.com/file/d/1fsC-qPfzYh72CzVPifpoBJGbS8XrbCC_/view?usp=sharing). The training took about 12 hours, during which it did 70k steps, which is 1.23 epochs, where the training loss dropped from 0.36 to 0.076.

 - For the second checkpoint the model is available [here](https://drive.google.com/file/d/1VK0yYGx_UQ9ugFhOwSeeu0sIAlnnt8hZ/view?usp=sharing). The training took about 18 hours, during which it did 100k steps, which is 1.65 epochs, where the training loss dropped from 0.36 to 0.070.


## Results
Four different metrics were used to evaluate the model: BLEU, ROUGEL, BERTscore and ParaScore. The results are shown in the table below. (The results are shown as mean±std.)

| Score      | Dataset           | Model(1.23)     | Model(1.65)     |
|------------|-------------------|-----------------|-----------------|
| BLUE       | 0.21±0.27         | 0.33±0.37       | 0.31±0.36       |
| ROUGEL     | 0.54±0.24         | 0.56±0.32       | 0.55±0.32       |
| BERTScore  | 0.97±0.02         | 0.95±0.05       | 0.95±0.05       |
| ParaScore  | 0.89±0.11         | 0.77±0.29       | 0.76±0.28       |

