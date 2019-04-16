from python_src import app
from python_src.viz import visualize_map
from python_src import db_connection as db_conn


visualize_map()
if __name__ == '__main__':
    app.run(debug=True)  #host='0.0.0.0', port=80)

