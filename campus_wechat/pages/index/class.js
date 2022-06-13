import drawQrcode from '../../utils/weapp.qrcode.js'
const app = getApp();

Page({

    /**
     * 页面的初始数据
     */
    data: {
        text: 'http://120.25.1.147:8000/api/punch_in',
        inputValue: '',
        result: '',
        regFlag: false
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (e) {
        this.checkLogin();
        console.log('out:' + this.data.regFlag)
        
        // this.draw();
        // wx.navigateTo({
        //     url: '/pages/login/index',
        // })
    },

    getScancode: function () {
        var that = this;
        wx.scanCode({
            onlyFromCamera: true,
            success: (res) => {
                var result = res.result;
                that.getRequestScancode(result)
            }
        })
    },

    getRequestScancode: function (result) {
        var that = this;

        var data = {token: app.getCache('token')};
        wx.request({
            url: result,
            method: 'POST',
            data: data,
            success: function (res) {
                console.log(res)
                that.setData({
                    result: result
                })
                wx.showToast({
                    title: "签到成功",
                    icon: 'success',
                    duration: 2000
                })
            }
        })
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    },
    draw() {
        drawQrcode({
            width: 160,
            height: 160,
            x: 20,
            y: 20,
            canvasId: 'myQrcode',
            // ctx: wx.createCanvasContext('myQrcode'),
            typeNumber: 10,
            text: this.data.text,
            image: {
                imageResource: '../../images/icon.png',
                dx: 70,
                dy: 70,
                dWidth: 60,
                dHeight: 60
            },
            callback(e) {
                console.log('e: ', e)
            }
        })
    },
    showAuth:function(){
        if (this.data.regFlag == false){
            var title = '为了更好的使用服务，请您先登录后再进行操作!';
            var content = '';
            wx.showModal({
                title: title,
                content: content,
                success(res) {
                    if (res.confirm) {
                        wx.navigateTo({
                            url: '/pages/index/index',
                        })
                    } else if (res.cancel) {
                        console.log('用户点击取消');
                    }
                }
            })
        }
    },
    checkLogin: function(){
        var that = this;
        wx.login({
            success:function(res){
                app.console("checkLogin");
                if(!res.code){
                    app.alert({
                        'content':'登录失败， 请再次点击'
                    })
                    return;
                }
                wx.request({
                    url: app.buildUrl("/member/check-reg"),
                    header: app.getRequestHeader(),
                    method: 'POST',
                    data: {code: res.code},
                    success:function(res){
                        if(res.data.code == 200){
                            // 微信授权且绑定学生信息
                            app.console("checkLogin is OK");
                            that.setData({
                                regFlag: true
                            })
                            app.console(that.data.regFlag);
                            app.setCache("token", res.data.data.token);
                        }else if(res.data.code == 1001){
                            // 微信已授权，但未绑定学生信息
                            wx.showModal({
                                title: '信息绑定',
                                content: '你还未进行信息绑定，是否进行绑定',
                                success (res) {
                                  if (res.confirm) {
                                    wx.navigateTo({
                                      url: '/pages/index/auth',
                                    })
                                  } else if (res.cancel) {
                                    console.log('用户点击取消')
                                  }
                                }
                              })
                        }else{
                            // 验证失败
                            app.console("checkLogin is fail");
                            app.alert({'content': res.data.msg});
                            that.setData({
                                regFlag:false
                            })
                            that.showAuth();
                            return;
                        }
                        
                    }
                })
            }
        })
    }
})