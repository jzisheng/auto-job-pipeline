
var mongoose = require("mongoose");
var passportLocalMongoose = require("passport-local-mongoose");

var JobListingSchema = new mongoose.Schema({
    title:String,
    company:String,
    description:String,
    keywords:[String]
});

UserSchema.plugin(passportLocalMongoose);

module.exports = mongoose.model("User",UserSchema);
