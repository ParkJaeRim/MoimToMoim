export default [
  {
    path: "",
    view: "Home",
    name: "home"
  },
  // 유저
  {
    path: "/signup",
    view: "accounts/Signup",
    name: "signup"
  },
  {
    path: "/update",
    view: "accounts/Update",
    name: "update"
  },
  {
    path: "/detail",
    view: "accounts/Detail",
    name: "detail"
  },
  {
    path: "/detailmain",
    view: "accounts/DetailMain",
    name: "detailmain"
  },
  // meeting
  {
    path: "/meeting",
    view: "meeting/MeetingList",
    name: "meetinglist"
  },
  {
    path: "/meeting/:m_id",
    view : "meeting/MeetingDetail",
    name : "meetingDetail"
  },
  // store
  {
    path: "/store/:s_id",
    view: "stores/StoreDetail",
    name: "storedetail"
  },
  // promise
  {
    path: "/promise/:m_id",
    view: "promise/MakePromise1",
    name: "makepromise1"
  },
  {
    path: "/promise2/:p_id",
    view: "promise/MakePromise2",
    name: "makepromise2"
  },
  // 코스 추가 수정 삭제
  {
    path: "/course",
    view: "promise/CourseEdit",
    name: "courseEdit"
  },

  {
    path: "/promise/:mid/create",
    view: "promise/MakePromise1",
    name: "makePromise"
  },
];
