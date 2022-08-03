if ("geolocation" in navigator) {
  /* 위치정보 사용 가능 */
} else {
  /* 위치정보 사용 불가능 */
}

const currentGeoLocation = document.getElementById("currentGeoLocation");

currentGeoLocation.onclick = function () {
  var startPos;
  var geoOptions = {
    timeout: 10 * 1000,
  };
  var element = document.getElementById("nudge");

  var showNudgeBanner = function () {
    nudge.style.display = "block";
  };

  var hideNudgeBanner = function () {
    nudge.style.display = "none";
  };

  var nudgeTimeoutId = setTimeout(showNudgeBanner, 5000);

  var geoSuccess = function (position) {
    hideNudgeBanner();
    // We have the location, don't display banner
    clearTimeout(nudgeTimeoutId);

    // Do magic with location
    startPos = position;
    document.getElementById("startLat").innerHTML = startPos.coords.latitude;
    document.getElementById("startLon").innerHTML = startPos.coords.longitude;
  };
  var geoError = function (error) {
    console.log("Error occurred. Error code: " + error.code);
    // error.code can be:
    //   0: unknown error
    //   1: permission denied
    //   2: position unavailable (error response from location provider)
    //   3: timed out
    switch (error.code) {
      case error.PERMISSION_DENIED:
        // The user didn't accept the callout
        document.getElementById("nudge").innerHTML =
          "위치정보 허용 권한이 없습니다";
        showNudgeBanner();
        break;
      case error.POSITION_UNAVAILABLE:
        // The user didn't accept the callout
        document.getElementById("nudge").innerHTML =
          "위치 정보를 가져오지 못했습니다";
        showNudgeBanner();
        break;
      case error.TIMEOUT:
        // The user didn't accept the callout
        document.getElementById("nudge").innerHTML = "시간 초과";
        showNudgeBanner();
        break;
    }
  };

  navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
};
