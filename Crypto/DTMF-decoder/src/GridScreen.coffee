React = require('react')
D = require('react-dynamics')

Hotkeyable = require('./Hotkeyable.coffee')
StreamValue = require('./StreamValue.coffee')
ToneTester = require('./ToneTester.coffee')

h = React.createElement

TestButton = ({ keyCode, frequency, inputNode, previewNode }) ->
  h Hotkeyable, keyCode: keyCode, contents: (keyState) => h D.Pressable, {}, (pressState) =>
    h ToneTester, frequency: frequency, inputNode: inputNode, previewNode: previewNode, on: keyState or pressState, contents: (testerState) =>
      h 'button', style: {
        boxSizing: 'border-box'
        display: 'inline-block'
        width: '40px'
        height: '30px'
        padding: '0'
        fontFamily: 'Courier New, mono'
        fontWeight: 'bold'
        fontSize: '12px'
        color: '#808080'
        lineHeight: '28px'
        textAlign: 'center'
        background: (if testerState then '#f8e8e0' else '#e0e0e0')
        cursor: 'pointer'
        border: '1px solid #c0c0c0'
        borderRadius: '5px'
        boxShadow: (if testerState then '0px 0px 10px -5px #000 inset' else '')
      }, 'TEST'

FrequencyCard = ({ frequency, detectorValue }) ->
  h 'span', style: {
    display: 'inline-block'
    verticalAlign: 'middle'
    fontFamily: 'Courier New, mono'
    fontWeight: 'bold'
    fontSize: '18px'
    color: '#404040'
    width: '80px'
    lineHeight: '38px'
    textAlign: 'center'
    border: '1px solid #c0c0c0'
    background: if detectorValue then '#e0ffe0' else '#fff'
    borderRadius: '5px'
  }, frequency + 'Hz'

CodeCard = ({ code, loDetectorValue, hiDetectorValue }) ->
  h 'span', style: {
    display: 'inline-block'
    verticalAlign: 'middle'
    fontFamily: 'Courier New, mono'
    fontWeight: 'bold'
    fontSize: '24px'
    color: '#404040'
    width: '60px'
    lineHeight: '38px'
    textAlign: 'center'
    border: '1px solid #c0c0c0'
    background: if loDetectorValue or hiDetectorValue then (if loDetectorValue and hiDetectorValue then '#ffe0e0' else '#e0e0e0') else '#fff'
    borderRadius: '5px'
  }, code

GridScreen = ({ loBank, hiBank, keyCodeListSet, coder, inputNode, previewNode, widthPx, heightPx }) ->
  tdStyle = { display: 'table-cell', verticalAlign: 'middle', textAlign: 'center', border: 0, padding: '10px', width: '80px', height: '40px' }
  tdLeadStyle = Object.assign {}, tdStyle, width: '140px'

  groupItems = {}
  for loDetector, lo in loBank
    groupItems['lo' + lo] = do(loDetector) -> (cb) -> h StreamValue, stream: loDetector.output, contents: (data) -> cb(data and data.value)
  for hiDetector, hi in hiBank
    groupItems['hi' + hi] = do(hiDetector) -> (cb) -> h StreamValue, stream: hiDetector.output, contents: (data) -> cb(data and data.value)

  h 'div', style: {
    display: 'inline-block'
    verticalAlign: 'middle'
    position: 'relative'
    width: widthPx + 'px'
    height: heightPx + 'px'
    overflow: 'hidden',
    border: '1px solid #c0c0c0'
    borderRadius: '3px'
  }, h D.GroupState, items: groupItems, (detectorStates) -> h 'div', style: {
    display: 'table'
    tableLayout: 'fixed'
    border: 0
    margin: '20px auto'
    padding: 0
    cellSpacing: 0
    lineHeight: '1em'
  }, (
    h 'div', style: { display: 'table-row' }, (
      h 'div', style: tdLeadStyle, ''
    ), (
      for hiDetector, hi in hiBank
        h 'div', key: hi, style: tdStyle,
          (h FrequencyCard, frequency: hiDetector.rms.frequency, detectorValue: detectorStates['hi' + hi]),
          (h 'div', style: { height: '10px' }),
          h TestButton, keyCode: keyCodeListSet[1][hi], frequency: hiDetector.rms.frequency, inputNode: inputNode, previewNode: previewNode
    )
  ), (
    for loDetector, lo in loBank
      h 'div', key: lo, style: { display: 'table-row' }, (
        h 'div', style: tdLeadStyle,
          (h FrequencyCard, frequency: loDetector.rms.frequency, detectorValue: detectorStates['lo' + lo]),
          (h 'div', style: { display: 'inline-block', verticalAlign: 'middle', width: '10px' }),
          h TestButton, keyCode: keyCodeListSet[0][lo], frequency: loDetector.rms.frequency, inputNode: inputNode, previewNode: previewNode
      ), (
        for hiDetector, hi in hiBank
          h 'div', key: hi, style: tdStyle,
            h CodeCard,
              loDetectorValue: detectorStates['lo' + lo],
              hiDetectorValue: detectorStates['hi' + hi],
              code: coder.getCode(lo, hi)
      )
  )

module.exports = GridScreen
