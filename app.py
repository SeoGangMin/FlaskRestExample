from flask_restful import Api;
from common import router;
app = router.app;

api = Api(app);

#Set Router
api.add_resource(router.Tag, '/tag', methods=["GET", "POST"]);
api.add_resource(router.Test, '/test', methods=["GET", "POST"]);

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000);
