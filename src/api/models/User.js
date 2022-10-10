const mongoose = require('mongoose');

const UserSchema = mongoose.Schema({
    googleId: {
        type: String
    },
    name: {
        type: String
    },
    email : {
        type: String,
        required: true
    },
    password: {
        type: String,
    },
    date: {
        type: Date,
        default: Date.now
    },
    profile_pic: {
        type: String
    }
});

module.exports = mongoose.model('User', UserSchema);
