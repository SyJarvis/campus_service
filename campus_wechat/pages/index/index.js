// index.js
// 获取应用实例
const app = getApp()

Page({
    data: {
        userInfo: {},
        remind: '加载中',
        angle: 0,
        regFlag: true

    },
    onLoad: function () {
        if (wx.getUserProfile) {
            this.setData({
                canIUseGetUserProfile: true
            })
        }

    },
    goToAuth: function () {
        wx.navigateTo({
            url: '/pages/index/auth',
        })
    },
    getUserProfile(e) {
        var that = this;
        // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认，开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
        wx.getUserProfile({
            desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
            success: (res) => {

                var data = res.userInfo
                console.log(res.userInfo)
                wx.login({

                    success(res) {
                        console.log(res);
                        console.log(res.code);
                        if (!res.code) {
                            app.alert({
                                'content': '登录失败，请再次点击'
                            })
                            return;
                        }
                        console.log("sss")
                        data['code'] = res.code;
                        wx.request({
                            url: app.buildUrl("/member/login"),
                            header: {
                                'content-type': 'application/x-www-form-urlencoded',
                            },
                            method: 'POST',
                            data: data,
                            success: function (res) {
                                if (res.data.code != 200) {
                                    console.log('error300')

                                } else {
                                    that.goToAuth();
                                    console.log('ok');
                                    console.log(res.data);
                                    app.setCache('token', res.data.data.token);
                                    console.log(res.data.data.token);
                                }
                            }
                        })
                    }
                })
            }
        })

    },
    click_tap: function () {
        app.alert({
            'content': '登录失败，请再次点击'
        })
    },
    BackIndex: function () {
        wx.navigateBack({
          delta: 1,
        })
    }

})