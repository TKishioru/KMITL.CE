const one_day = 1000 * 60 * 60 * 24;

function RFM_show(output_ID,start_select, end_select) {
    var dataFields = new Array();
    let rfm_output = '';
    rfm_output += '<table id="rfm_output" class="table table-striped table-bordered">';
    rfm_output += '<tr><th rowspan="2">Username</th><th colspan="3">RFM - model</th><th rowspan="2">Result</th></tr>';
    rfm_output += '<tr><th>R</th><th>F</th><th>M</th></tr>';
    //summary

    let allData = {allRecency: [], allFrequency: [], allMonetary: []}
    for (let i = 0; i < dataofuser.length; i++) {
        var a = PRIMARYanalysis(dataofuser[i].name, dataofuser[i].transactions, start_select, end_select);
        if (a.Lastdate != -1) {
            allData.allRecency.push(a.Lastdate);
            allData.allFrequency.push(a.Freq);
            allData.allMonetary.push(a.Total);
        }
        dataFields.push(a);
    }
    let rank = { R_rank: PERCENTRANK(allData.allRecency), F_rank: PERCENTRANK(allData.allFrequency), M_rank: PERCENTRANK(allData.allMonetary) };
    //display
    //return { Name: name, Lastdate: -1.0, Total: -1.0, Freq: -1.0 };
    for (let i = 0; i < dataFields.length; i++) {
        if (dataFields.Lastdate == -1) {
            rfm_output += '<tr>';
            rfm_output += "<td>" + dataFields[i].name + "</td>";
            rfm_output += "<td>0 %</td>";
            rfm_output += "<td>0 %</td>";
            rfm_output += "<td>0 %</td>";
            rfm_output += "<td>ไม่ได้อยู่ในช่วงเวลาที่เลือก</td>";
            rfm_output += '</tr>';

            csvFileData.push([dataFields[i].name, "ไม่ได้อยู่ในช่วงเวลาที่เลือก"]);
        }
        else {
            var tempUser = rankRFM(dataFields[i], rank, dataFields.length);
            rfm_output += '<tr>';
            rfm_output += "<td>" + tempUser.Name + "</td>";
            rfm_output += "<td>" + tempUser.Recency + " %</td>";
            rfm_output += "<td>" + tempUser.Frequency + " %</td>";
            rfm_output += "<td>" + tempUser.Monetary + " %</td>";
            var tempRFM = convertRFM(Math.ceil(tempUser.Recency / 20), Math.ceil(tempUser.Frequency / 20), Math.ceil(tempUser.Monetary / 20));
            rfm_output += "<td>" + tempRFM + "</td>";
            rfm_output += '</tr>';
            console.log(dataofuser[i].name, " : ", tempUser, " >> ", tempRFM);
            csvFileData.push([dataFields[i].name, tempRFM]);
        }

    }
    rfm_output += '</table>';
    //console.log(csvFileData);
    document.getElementById(output_ID).innerHTML = rfm_output;
    return csvFileData;
}

function PRIMARYanalysis(name, data, start_select, end_select) {
    var Result = { Name: name, Lastdate: 0.0, Total: 0.0, Freq: 0.0 };
    
    //Time
    data.sort(function (a, b) { return new Date(a[0]) - new Date(b[0]); });
    start_select.setHours(0, 0, 0, 0);
    end_select.setHours(0, 0, 0, 0);
    let start_datareal = data[0][0];
    let end_datareal = data[data.length - 1][0];

    if (((start_datareal < start_select) && (end_datareal < start_select)) || ((start_datareal > end_select) && (end_datareal > end_select))) {
        return { Name: name, Lastdate: -1.0, Total: -1.0, Freq: -1.0 };
    }

    //Recency_percent + Frequency_percent + Monetary_percent
    for (let i = 0; i < data.length; i++) {
        if (start_select <= data[i][0] && data[i][0] <= end_select) {
            Result.Lastdate = data[i][0];
            Result.Total += data[i][1];
            Result.Freq++;
        }
    }
    Result.Total = Result.Total.toFixed(2);
    return Result;
}



function rankRFM(datafields, rank, len) {
    console.log("datafields", datafields, "rank", rank, "len", len)
    return {
        Recency: PERCENTRANK_INC(datafields.Lastdate, rank.R_rank, len),
        Frequency: PERCENTRANK_INC(datafields.Freq, rank.F_rank, len),
        Monetary: PERCENTRANK_INC(datafields.Total, rank.M_rank, len)
    };
}


function sendvalue(r, c) {
    return table.rows[r].cells[c].innerHTML;
    //return document.getElementById(input).value;
}
function segment_findnumof(output_ID) {
    var result = document.getElementById(output_ID);
    var chart_data = new Array();
    var segment_name = new Array();

    for (let i = 2; i < result.rows.length; i++) {
        if (segment_name.indexOf(result.rows[i].cells[4].innerHTML) == -1) {
            //chart_data.findIndex(x => x.segment === tempRFM) == -1
            segment_name.push(result.rows[i].cells[4].innerHTML);
            chart_data.push({ segment: result.rows[i].cells[4].innerHTML, numberof: 1 });
        }
        else {
            for (let j = 0; j < segment_name.length; j++) {
                if (chart_data[j].segment == result.rows[i].cells[4].innerHTML) {
                    chart_data[j].numberof++;
                }
            }
        }
    }
    return chart_data;
}
function convertRFM(R, F, M) {
    R = R == 0 ? 1 : R;
    F = F == 0 ? 1 : F;
    M = M == 0 ? 1 : M;

    console.log("RFM:", R, F, M);
    for (let i = 3; i < table.rows.length; i++) {
        //console.log(table.rows[i].cells[1].innerHTML);
        if ((R >= sendvalue(i, 1) && R <= sendvalue(i, 2)) && (F >= sendvalue(i, 3) && F <= sendvalue(i, 4)) && (M >= sendvalue(i, 5) && M <= sendvalue(i, 6))) {
            return table.rows[i].cells[0].innerHTML;
        }
    }
    return 'ไม่จัดอยู่ในกลุ่มใด';
}

//Statistics
function PERCENTRANK(data) {
    var Setrank = {};
    data.sort(function (a, b) { return a - b });

    for (let i = 0; i < data.length; i++) {
        const item = data[i];

        if (!Setrank[item]) {
            Setrank[item] = i;
        }
    }
    return Setrank;
}
function PERCENTRANK_INC(val, Setrank, len) {
    return (Setrank[val] / (len - 1) * 100).toFixed(2);
}