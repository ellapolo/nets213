var mongo = require ('./mongo');

module.exports = {
  addUpdate: function (id, new_update, callback) {
    mongo.Update.findById(id, function(error, update) {
      if (error) {
        update = new mongo.Update({_id:id, name_update: null, menu_update: [new_update]});
      } else {
        var seen = false;
        for (var up in update.menu_update) {
          if (new_update.item == up.item and new_update.price == up.price) {
            up.votes = up.votes + 1;
            seen = true;
          }
        }
        if (!seen) {
          update.menu_update.push(new_update);
        }
      }
      update.save(function (error) {
        callback(error, tid);
      });
    });    
  },

  getUpdate: function (_id, callback) {
    mongo.Update.findById(_id, function (error, product) {
      callback(error, update);
    });
  },

};