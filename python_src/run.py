from python_src import app
from python_src.viz import visualize_map


visualize_map(label_nodes=True)
if __name__ == '__main__':
    app.run(debug=True)  #host='0.0.0.0', port=80)

