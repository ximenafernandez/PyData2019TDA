import matplotlib.pyplot as plt
import numpy as np

def visualize_scatter(data_2d, labels, figsize=(10,5)):

    plt.figure(figsize=figsize)
    
    nb_classes = len(np.unique(labels))
    
    label_to_id_dict = {v:i for i,v in enumerate(np.unique(labels))}
    id_to_label_dict = {v: k for k, v in label_to_id_dict.items()}
    label_ids = np.array([label_to_id_dict[x] for x in labels])
    
    for label_id in np.unique(label_ids):
        plt.scatter(data_2d[np.where(label_ids == label_id), 0],
                    data_2d[np.where(label_ids == label_id), 1],
                    marker='o',
                    color= plt.cm.gist_rainbow(label_id / float(nb_classes)),
                    linewidth='1',
                    alpha=0.4,
                    label=id_to_label_dict[label_id])
        ax = plt.gca()
    plt.legend(loc='best')
    
    ax.set_facecolor('xkcd:black')