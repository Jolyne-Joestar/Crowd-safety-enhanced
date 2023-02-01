"""
Script to visualize the prediction results alongside the casting images
"""

import csv

import cv2
import matplotlib.pyplot as plt

CSV_FILE = "casting_predictions_010223-12-33-21.csv"  # change file name accordingly
INSPECTION_IMGS_DIR = "castings_data/inspection/"
RESULTS_FILE = "inspection_results.png"

fig, axs = plt.subplots(2, 5, figsize=(50, 20))

with open(CSV_FILE) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=",")
   next(csv_reader, None)
   for i, row in enumerate(csv_reader):
      # csv columns follow this order: 'Time', 'filename', 'pred_label', 'pred_score'
      image_path = INSPECTION_IMGS_DIR + row[1]
      image_orig = cv2.imread(image_path)
      image_orig = cv2.cvtColor(image_orig, cv2.COLOR_BGR2RGB)

      row_idx = 0 if i < 5 else 1
      axs[row_idx][i % 5].imshow(image_orig)
      axs[row_idx][i % 5].set_title(row[1] + " - " + row[2], fontsize=35)
      axs[row_idx][i % 5].axis("off")

fig.savefig(RESULTS_FILE)