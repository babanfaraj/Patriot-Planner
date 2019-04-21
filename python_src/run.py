from python_src import app

if __name__ == '__main__':
    on_ec2 = False  # True if the application is running on an EC2 instance
    if on_ec2:
        app.run(host='0.0.0.0', port=80)  # Note: must run as admin
    else:
        app.run(debug=True)

