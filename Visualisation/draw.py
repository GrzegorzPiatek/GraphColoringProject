import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def plotGraph(edges_dict):
    # Build a dataframe with your connections
    df = pd.DataFrame(edges_dict)

    # And a data frame with characteristics for your nodes
    carac = pd.DataFrame(
        {'ID': ['A', 'B', 'C', 'D', 'E'], 'myvalue': ['group1', 'group1', 'group2', 'group3', 'group3']})

    # Build your graph
    G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

    # The order of the node for networkX is the following order:
    G.nodes()
    # Thus, we cannot give directly the 'myvalue' column to netowrkX, we need to arrange the order!

    # Here is the tricky part: I need to reorder carac to assign the good color to each node
    carac = carac.set_index('ID')
    carac = carac.reindex(G.nodes())

    # And I need to transform my categorical column in a numerical value: group1->1, group2->2...
    carac['myvalue'] = pd.Categorical(carac['myvalue'])
    carac['myvalue'].cat.codes

    # Custom the nodes:
    nx.draw(G, with_labels=True, node_color=carac['myvalue'].cat.codes, cmap=plt.cm.Set1, node_size=1500)
    plt.show()
