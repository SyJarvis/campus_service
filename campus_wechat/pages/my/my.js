
const app = getApp();
// pages/my/my.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        userInfo:{
            'avatarUrl': 'https://thirdwx.qlogo.cn/mmopen/vi_32/Ntu9fwwtR57BELQ0wzT4Gia1pIAC82pwqSOoppt0ps6B9PIuW9aqVj9zYLofAAbZJZy0tcOIdelXcklKGuvql2w/132',
            'nickName': '上邪s',
            'stu_num': '202103130460',
            'drom_name': '广东工贸职业技术学院西区1号201宿舍s'
        }
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {
        this.userInfo();
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady() {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow() {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide() {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload() {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh() {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom() {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage() {

    },
    navQcrode(){
        wx.navigateTo({
          url: '/pages/my/drowqcrode',
        })
    },
    userInfo:function(){
        var that = this;
        wx.request({
            url: app.buildUrl("/my/info"),
            header: app.getRequestHeader(),
            method: 'POST',
            success:function(res){
                if (res.data.code != 200){
                    app.alert({'content': res.data.msg});
                    return;
                }
                that.setData({
                    userInfo: res.data.data
                })
                console.log("okkk")
            }
        })
    }
    
})